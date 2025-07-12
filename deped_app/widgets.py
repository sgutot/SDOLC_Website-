class AdminDateTimeWidget(forms.DateTimeInput):
    template_name = 'admin/widgets/datetime.html'
    
    def __init__(self, attrs=None, format=None):
        attrs = {'type': 'datetime-local', 'class': 'form-control'}
        super().__init__(attrs=attrs, format=format)