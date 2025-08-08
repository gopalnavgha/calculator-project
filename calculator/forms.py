from django import forms

OP_CHOICES = [
    ('add', 'Addition'),
    ('sub', 'Subtraction'),
    ('mul', 'Multiplication'),
    ('div', 'Division'),
    ('power', 'Power'),
    ('square', 'Square'),
    ('sqrt', 'Square Root'),
    ('area_rect', 'Area Rectangle'),
    ('area_circle', 'Area Circle'),
    ('area_tri', 'Area Triangle'),
    ('quad_roots', 'Quadratic Roots'),
    ('simple_int', 'Simple Interest'),
    ('compound_int', 'Compound Interest'),
    ('bmi', 'BMI'),
    ('distance', 'Distance Between Points'),
]

class CalcForm(forms.Form):
    operation = forms.ChoiceField(choices=OP_CHOICES)
    x = forms.FloatField(required=False)
    y = forms.FloatField(required=False)
    z = forms.FloatField(required=False)
    t = forms.FloatField(required=False)
    n = forms.IntegerField(required=False)
    x1 = forms.FloatField(required=False)
    y1 = forms.FloatField(required=False)
    x2 = forms.FloatField(required=False)
    y2 = forms.FloatField(required=False)

    def clean(self):
        cleaned = super().clean()
        op = cleaned.get('operation')
        if op in ('add','sub','mul','div','power'):
            if cleaned.get('x') is None or cleaned.get('y') is None:
                raise forms.ValidationError('x आणि y द्या')
        if op == 'sqrt' and cleaned.get('x') is None:
            raise forms.ValidationError('x द्या')
        if op == 'area_rect' and (cleaned.get('x') is None or cleaned.get('y') is None):
            raise forms.ValidationError('length आणि width द्या')
        if op == 'area_circle' and cleaned.get('x') is None:
            raise forms.ValidationError('radius द्या')
        if op == 'area_tri' and (cleaned.get('x') is None or cleaned.get('y') is None):
            raise forms.ValidationError('base आणि height द्या')
        if op == 'quad_roots' and (cleaned.get('x') is None or cleaned.get('y') is None or cleaned.get('z') is None):
            raise forms.ValidationError('a,b,c द्या')
        if op == 'simple_int' and (cleaned.get('x') is None or cleaned.get('y') is None or cleaned.get('z') is None):
            raise forms.ValidationError('P,R,T द्या')
        if op == 'compound_int' and (cleaned.get('x') is None or cleaned.get('y') is None or cleaned.get('z') is None):
            raise forms.ValidationError('P,R,T द्या')
        if op == 'bmi' and (cleaned.get('x') is None or cleaned.get('y') is None):
            raise forms.ValidationError('weight आणि height द्या')
        if op == 'distance' and (cleaned.get('x1') is None or cleaned.get('y1') is None or cleaned.get('x2') is None or cleaned.get('y2') is None):
            raise forms.ValidationError('x1,y1,x2,y2 द्या')
        return cleaned
