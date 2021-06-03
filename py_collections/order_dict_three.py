from collections import OrderedDict


order = OrderedDict()
order['team'] = 'qatar'
order['ranking'] = 58
order['confederation'] = 'afc'
for k,v in order.items():
    print(f'{str(k).title()} :-: {str(v).title()}')

