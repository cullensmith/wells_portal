import csv
from django.core.management.base import BaseCommand
from portal.models import Well

class Command(BaseCommand):
    help = 'Load well data from a CSV file into the database'

    def handle(self, *args, **kwargs):
        with open('E:\\CMapS\\fractracker\\project_data\\wells/welllocs_out500.csv', mode='r') as file:

            reader = csv.DictReader(file)
            ctr = 0
            for row in reader:
                ctr+=1
                Well.objects.create(
                    api_num=row['api_num'],
                    other_id=row['other_id'],
                    latitude=float(row['latitude']),
                    longitude=float(row['longitude']),
                    stusps=row['stusps'],
                    county=row['county'],
                    municipality=row['municipality'],
                    well_name=row['well_name'],
                    operator=row['operator'],
                    spud_date=row['spud_date'],
                    plug_date=row['plug_date'],
                    well_type=row['well_type'],
                    well_status=row['well_status'],
                    well_configuration=row['well_configuration'],
                    ft_category=row['ft_category'],
                    wellwiki=row['wellwiki'],
                    src_url=row['src_url'],
                    ftuid=float(row['ftuid']),
                    # id=float(row['id']),
                    lat=row['lat'],
                    lng=row['lng']
                )
                if ctr%1000==0 or ctr == 0:
                    print(f'made it to: {ctr}')
                    print('==========================')
                    print('==========================')
        self.stdout.write(self.style.SUCCESS('Successfully imported well data'))
