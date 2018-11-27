states = '''Alabama 
Alaska 
Arizona 
Arkansas 
California 
Colorado 
Connecticut 
Delaware 
District-of-Columbia
Florida 
Georgia 
Hawaii 
Idaho 
Illinois
Indiana 
Iowa 
Kansas 
Kentucky 
Louisiana 
Maine 
Maryland 
Massachusetts 
Michigan 
Minnesota 
Mississippi 
Missouri 
Montana
Nebraska 
Nevada 
New-Hampshire 
New-Jersey 
New-Mexico 
New-York 
North-Carolina 
North-Dakota 
Ohio 
Oklahoma 
Oregon 
Pennsylvania 
Rhode-Island 
South-Carolina 
South-Dakota 
Tennessee 
Texas 
Utah 
Vermont 
Virginia 
Washington 
West-Virginia 
Wisconsin 
Wyoming
'''

states = states.split()
states = [state.replace('-', ' ') for state in states]

url = 'http://www.countyhealthrankings.org/sites/default/files/state/downloads/'
import urllib.request
for state in states:
    print(state)
    urlend = '2018%20County%20Health%20Rankings%20{}%20Data%20-%20v1.xls'.format(state.replace(' ', '%20'))
    if state in ['Michigan', 'Missouri']:
        urlend = '2018%20County%20Health%20Rankings%20{}%20Data%20-%20v1_0.xls'.format(state.replace(' ', '%20'))
    urllib.request.urlretrieve('{}{}'.format(url, urlend), '{}.xls'.format(state.replace(' ', '-').lower()))

