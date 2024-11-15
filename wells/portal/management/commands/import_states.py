import csv
from django.core.management.base import BaseCommand
from portal.models import States

class Command(BaseCommand):
    help = 'Load well data from a CSV file into the database'

    def handle(self, *args, **kwargs):
        with open('E:\\CMapS\\fractracker\\project_data\\wells/states_json.csv', mode='r') as file:

            reader = csv.DictReader(file)
            ctr = 0
            for row in reader:
                ctr+=1
                States.objects.create(
                    geomjson=row['geomjson'],
                    statename=row['statename'],
                    
                )
                if ctr%1000==0 or ctr == 0:
                    print(f'made it to: {ctr}')
                    print('==========================')
                    print('==========================')
        self.stdout.write(self.style.SUCCESS('Successfully imported well data'))
