from django.shortcuts import render
from .models import Well
# from .models import Counties, States, Wells_OH, Wells_PA, Wells_TX
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from django.core.serializers import serialize
from django.db.models import Q
import json 
import ast



# Create your views here.
def portal(request):
    well = Well.objects.all()
    return render(request, 'home.html', { 'portal': portal })

def getstates_view(request):
    print('now were getting the states for the map')
    print(f'here is the request: {request}')
    print(f"states requested: {request.GET.getlist('states')}")
    states_in = request.GET.getlist('states')[0].split(',')
    print(f'states in = {states_in}')
    states = list()
    for s in states_in:
        h = s.strip()
        # states.append(h)
        # states.append(h.upper())
        # states.append(h.lower())
        states.append(h.title())
    print(f"states--{len(states)}->{states}")
    filter_kwargs = dict()
    # if len(states) == 1:
    #     filter_kwargs.update(f'statename__iexact={states}')
    # else:
    # for getstate in states:
        
    filter_kwargs.update({'statename__in':states})

    print(f'the query = {filter_kwargs}')
    polygons = States.objects.filter(**filter_kwargs)  # Query all polygons
    print(f'state polygons-_-_-_-->{polygons}')
    features = []
    for i,polygon in enumerate(polygons):
        # if i > 5:
        #     break
        # Parse GeoJSON text from the geomjson field
        geojson_data = polygon.geomjson
        # Add GeoJSON feature to the list
        feature = dict()
        feature['type'] = "Feature"
        feature['properties'] = {}
        feature['geometry'] = ast.literal_eval(geojson_data)
        features.append(feature)
        # print('so we got here')
        
    # Create GeoJSON FeatureCollection
    geojson_collection = {
        "type": "FeatureCollection",
        "features": features
    }
    # print(geojson_collection)
    return JsonResponse(geojson_collection)


def getcounties_view(request):
    print('now were getting the counties for the map')
    print(f'here is the request: {request}')
    print(f"states requested: {request.GET.getlist('states')}")
    states_in = request.GET.getlist('states')[0].split(',')
    print(f'states in = {states_in}')
    states = list()
    for s in states_in:
        h = s.strip()
        # states.append(h)
        # states.append(h.upper())
        # states.append(h.lower())
        states.append(h.title())
    print(f"states--{len(states)}->{states}")
    filter_kwargs = dict()
    # if len(states) == 1:
    #     filter_kwargs.update(f'statename__iexact={states}')
    # else:
    # for getstate in states:
        
    filter_kwargs.update({'statename__in':states})

    print(f'the query = {filter_kwargs}')
    polygons = Counties.objects.filter(**filter_kwargs)  # Query all polygons
    features = []
    for i,polygon in enumerate(polygons):
        # if i > 5:
        #     break
        # Parse GeoJSON text from the geomjson field
        geojson_data = polygon.geomjson
        # Add GeoJSON feature to the list
        feature = dict()
        feature['type'] = "Feature"
        feature['properties'] = {}
        feature['geometry'] = ast.literal_eval(geojson_data)
        features.append(feature)
        # print('so we got here')
        
    # Create GeoJSON FeatureCollection
    geojson_collection = {
        "type": "FeatureCollection",
        "features": features
    }
    # print(geojson_collection)
    return JsonResponse(geojson_collection)

def update_table():
    # selected_dataset = request.GET.getlist('selectedDataset[]')
    # cols=list()
    print('==================================================\n=================================')
    cols = ["api_num",
            "other_id",
            "latitude",
            "longitude",
            "stusps",
            "county",
            "municipality",
            "well_name",
            "operator",
            "spud_date",
            "plug_date",
            "well_type",
            "well_status",
            "well_configuration",
            "ft_category"]
    new_table = generate_new_table(cols)
    return HttpResponse(new_table)

def generate_new_table(cols):
    # Simulate generating a new table
    cols = ["api_num",
            "other_id",
            "latitude",
            "longitude",
            "stusps",
            "county",
            "municipality",
            "well_name",
            "operator",
            "spud_date",
            "plug_date",
            "well_type",
            "well_status",
            "well_configuration",
            "ft_category"]
    new_table_html = "<tr>"
    # print(f'here are the columns{cols}')
    for i in cols:
        new_table_html += f"<th>{i}</th>"
    new_table_html += "</tr>"
    for i in range(1, 2):
        new_table_html += "<tr>"
        for j in range(1, len(cols)+1):
            if j in (1,len(cols)):
                continue
            new_table_html += f"<td>Row {i} Data {j}</td>"
        new_table_html += "</tr>"
    return new_table_html

def generate_geojson(request):
    print('now were getting the data for the map')
    print(f'here is the request: {request}')
    print(f"states requested: {request.GET.getlist('states')}")
    states_in = request.GET.getlist('states')[0].split(',')
    states = list()
    for s in states_in:
        h = s.strip()
        # states.append(h)
        # states.append(h.upper())
        # states.append(h.lower())
        states.append(h.title())
    states = list(set(states))
    cats = list()
    # counties = list()
    well_status_in = request.GET.getlist('well_status')[0].split(',')
    well_status = list()
    for s in well_status_in:
        h = s.strip()
        well_status.append(h)
        well_status.append(h.upper())
        well_status.append(h.lower())
        well_status.append(h.title())
    well_status = list(set(well_status))
    well_type_in = request.GET.getlist('well_type')[0].split(',')
    well_type = list()
    for s in well_type_in:
        h = s.strip()
        well_type.append(h)
        well_type.append(h.upper())
        well_type.append(h.lower())
        well_type.append(h.title())
    well_type = list(set(well_type))
    well_name_in = request.GET.getlist('well_name')[0].split(',')
    well_name = list()
    for s in well_name_in:
        h = s.strip()
        well_name.append(h)
        well_name.append(h.upper())
        well_name.append(h.lower())
        well_name.append(h.title())
    well_name = list(set(well_name))
    category = request.GET.getlist('category')
    fcats = list()
    catsplit = category[0].split(',')
    print(f'here is catsplit -->{catsplit}')
    if 'default' in catsplit or 'initial' in catsplit:
        fcats.append('default')
    elif catsplit == ['']:
        fcats.append('default')
    else:
        for c in category[0].split(','):
            fcats.append(c)
    stateop = request.GET.getlist('statesop')
    county_in = request.GET.getlist('county')[0].split(',')
    county = list()
    for s in county_in:
        h = s.strip()
        # # h = s.replace('County','').replace('COUNTY','').strip()
        # print(f'the county records are: {h}')
        # print('****************************=')
        # h = s.strip()
        h = s.replace('County','').replace('COUNTY','').replace('county','').strip()
        print(f'the new county records are: {h}')
        print('===============================')
        county.append(h)
        county.append(h.upper())
        # county.append(h.lower())
        county.append(h.title())
    county = list(set(county))
    ctyop = request.GET.getlist('countyop')
    wtop = request.GET.getlist('well_typeop')
    wsop = request.GET.getlist('well_statusop')
    wnop = request.GET.getlist('well_nameop')

    filterop_dict = {'states':['stusps',stateop,states], 
                     'well_status':['well_status',wsop,well_status],
                     'well_type':['well_type',wtop,well_type],
                     'well_name':['well_name',wnop,well_name],
                     'county':['county',ctyop,county],
                     'category':['category','',fcats]
                    }

    
    filter_dict = { 
                   'county':county, 
                   'well_status':well_status, 
                   'well_type':well_type, 
                   'well_name':well_name, 
                   }

    filter_kwargs = dict()

    print(f'here is the main dict: {filterop_dict}')

    for k,v in filterop_dict.items():
        # print(f'here is the first layer: {k} and v: {v}')
        # print('======================================')
        # h = str(f)
        for s in v:
            if len(s) > 0:
                # print(f'here if v: {v}')
                # print(f'here if s: {s}')
                # print(f'here is k: {k}')
                if k == 'states':
                    aval = filterop_dict[k]
                    # print(f'the states aval = {aval}')
                    # if len(aval[2])>2:
                    filter_kwargs.update({f'{aval[0]}__in':aval[2]})
                # else:
                elif k in filter_dict.keys():
                    aval = filterop_dict[k]
                    # print(f'avalue= {aval}')
                    # print(f'opt={filterop_dict[k]}')
                    if aval[1] == ['default']:
                        # filter_kwargs.update({f'{aval[0]}__in':aval[2][0]})
                        continue
                    elif aval[1] == ['initial']:
                        filter_kwargs.update({f'{aval[0]}__iexact':aval[2][0]})
                    elif aval[1] == ['option2']:
                        filter_kwargs.update({f'{aval[0]}__in':aval[2]})
                    elif aval[1] == ['option3']:
                        filter_kwargs.update({f'{aval[0]}__icontains':aval[2][0]})
                    elif aval[1] == ['option4']:
                        filter_kwargs.update({f'{aval[0]}__istartswith':aval[2][0]})
                    # elif aval[1] == ['initial'] and aval[2] != ['Abandoned']:
                    #     continue
                    # else:
                    #     filter_kwargs.update({f'{aval[0]}__in':aval[2]})
                elif k == 'category':
                    print('here is what we are looking at')
                    print(k)
                    print(filterop_dict[k])
                    here = filterop_dict[k][2]
                    print(here)
                    print(aval[2])
                    if here == ['default']:
                        continue
                    else:
                        filter_kwargs.update({f'ft_category__in':here})

    print(f'kwargs = {filter_kwargs}')
    attrvals = list()
    # for u in filter_kwargs['stusps__in']:
    #     if u == 'pennsylvania':
    #         if len(filter_kwargs)>1:
    #             attrvals.extend(Wells_PA.objects.filter(**filter_kwargs))
    #         else:
    #             attrvals.extend(Wells_PA.objects.all())
    #         print('got pa!!!!!!!!!!!!')
    #     elif u == 'ohio':
    #         if len(filter_kwargs)>1:
    #             attrvals.extend(Wells_OH.objects.filter(**filter_kwargs))
    #         else:
    #             attrvals.extend(Wells_OH.objects.all())
    #         print('retrieved ohio!!!!!!!!!!')
    #     elif u == 'texas':
    #         attrvals.extend(Wells_TX.objects.filter(**filter_kwargs))   
    
    attrvals = Well.objects.filter(**filter_kwargs)
    print('got to here')

    newwell = list()
    for n,x in enumerate(attrvals):
        # if n<=5:
        tmp=vars(x)
        tmp.pop('_state')
        newwell.append(tmp)
    # newwells = json.dumps(newwell)
    print(f'newwells')
    geojson = {
        "type": "FeatureCollection",
        "features": [
        {
            "type": "Feature",
            "geometry" : {
                "type": "Point",
                "coordinates": [d["lng"], d["lat"]],
                },
            "properties" : d,
        } for d in newwell]
    }

    mapdata = json.dumps(geojson)
    return JsonResponse(mapdata, safe=False)






