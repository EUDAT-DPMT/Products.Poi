areas = list(context.getAvailableAreas())
areas.sort(lambda x,y: cmp(x['title'], y['title']))
return areas

