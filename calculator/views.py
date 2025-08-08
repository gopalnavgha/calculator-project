from django.shortcuts import render
from .forms import CalcForm
from . import calculators

OP_TO_FUNC = {
    'add': lambda d: calculators.add(d['x'], d['y']),
    'sub': lambda d: calculators.sub(d['x'], d['y']),
    'mul': lambda d: calculators.mul(d['x'], d['y']),
    'div': lambda d: calculators.div(d['x'], d['y']),
    'power': lambda d: calculators.power(d['x'], d['y']),
    'square': lambda d: calculators.square(d['x']),
    'sqrt': lambda d: calculators.sqrt(d['x']),
    'area_rect': lambda d: calculators.area_rectangle(d['x'], d['y']),
    'area_circle': lambda d: calculators.area_circle(d['x']),
    'area_tri': lambda d: calculators.area_triangle(d['x'], d['y']),
    'quad_roots': lambda d: calculators.quadratic_roots(d['x'], d['y'], d['z']),
    'simple_int': lambda d: calculators.simple_interest(d['x'], d['y'], d['z']),
    'compound_int': lambda d: calculators.compound_interest(d['x'], d['y'], d['z'], n=int(d.get('n') or 1)),
    'bmi': lambda d: calculators.bmi(d['x'], d['y']),
    'distance': lambda d: calculators.distance(d['x1'], d['y1'], d['x2'], d['y2']),
}

def index(request):
    result = None
    error = None
    if request.method == 'POST':
        form = CalcForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            op = data['operation']
            try:
                res = OP_TO_FUNC[op](data)
                result = res
            except Exception as e:
                error = str(e)
        else:
            error = form.errors.as_text()
    else:
        form = CalcForm()
    return render(request, 'calculator/index.html', {'form': form, 'result': result, 'error': error})
