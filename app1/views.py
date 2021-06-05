from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

cuotas = [
    {
        'monto': 1500,
        'tasa': 15,
        'plazo': 1,
        'cuota': 135.39,
        'total': 1624.68

    }
]


def calculo(request):
    if request.method == 'POST':
        monto = int(request.POST.get('monto'))
        tasa = int(request.POST.get('tasa'))
        plazo = int(request.POST.get('plazo'))
        cuota = (monto*((tasa/100)/12)/(1-(1+((tasa/100)/12))**(-plazo*12)))
        total = cuota*(plazo*12)

        ctx = {
            'cuotas': cuotas
        }

        cuotas.append({
            'monto': monto,
            'tasa': tasa,
            'plazo': plazo,
            'cuota': cuota,
            'total': total,
        })

        return render(request, 'formularios/index.html', ctx)
    else:
        ctx = {
            'cuotas': cuotas
        }

        return render(request, 'formularios/index.html', ctx)
