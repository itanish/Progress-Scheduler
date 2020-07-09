from django import forms
# from s3direct.widgets import S3DirectWidget

# class add_item_form(forms.ModelForm):
#     # video = forms.URLField(widget=S3DirectWidget(dest='example_destination'))

#     class Meta:
#         model = Item
#         fields = ['title','price','discount_price','category','description','image','image2']
#         exclude = ['slug']
#         widgets = {
#             'title' : forms.TextInput(attrs={
#                 'class' : 'form-control'
#             }), 
            
#             'price' : forms.NumberInput(attrs={
#                 'class' : 'form-control'
#             }),

#             'discount_price' : forms.NumberInput(attrs={
#                 'class' : 'form-control'
#             }),

#             'category' : forms.Select(attrs={
#                 'class' : 'form-control'
#             }),

#             'label' : forms.Select(attrs={
#                 'class' : 'form-control'
#             }),

#             # 'slug' : forms.TextInput(attrs={
#             #     'class' : 'form-control'
#             # }),

#             'description' : forms.TextInput(attrs={
#                 'class' : 'form-control'
#             }),

#             'image' : forms.FileInput(attrs={
#                 'class' : 'form-control',
#                 'style' :'opacity :1; position:static;'
#             }),

#             'image2' : forms.FileInput(attrs={
#                 'class' : 'form-control',
#                 'style' :'opacity :1; position:static;'
#             }),
#         }

#     def __init__(self, *args, **kwargs):
#             super(add_item_form, self).__init__(*args, **kwargs)
#             if self.instance:
#                 # If the instance has no image, they haven't uploaded anything
#                 if self.instance.image2 is None:
#                     # Alter the field in the form
#                     self.fields['image2'].disabled = True

# class front_banner_form(forms.ModelForm):
#     # video = forms.URLField(widget=S3DirectWidget(dest='example_destination'))

#     class Meta:
#         model = front_banner
#         fields = ['image']
#         widgets = {
#             'image' : forms.FileInput(attrs={
#                 'class' : 'form-control',
#                 'style' :'opacity :1; position:static;'
#             }),

#         }
        
# class contact_form(forms.ModelForm):
#     # video = forms.URLField(widget=S3DirectWidget(dest='example_destination'))

#     class Meta:
#         model = Contact
#         fields = ['user','contactno']
#         exclude = ['user','contactno']

# class lower_banner_form(forms.ModelForm):
#     # video = forms.URLField(widget=S3DirectWidget(dest='example_destination'))

#     class Meta:
#         model = lower_banner
#         fields = ['image2']
#         widgets = {
#             'image2' : forms.FileInput(attrs={
#                 'class' : 'form-control',
#                 'style' : 'opacity :1; position:static;'
#             }),

#         }

# class coupon_form(forms.ModelForm):
#     # video = forms.URLField(widget=S3DirectWidget(dest='example_destination'))

#     class Meta:
#         model = Coupon
#         fields = ['code','amount']
#         widgets = {
#             'code' : forms.TextInput(attrs={
#                 'class' : 'form-control'
#             }), 
            
#             'amount' : forms.NumberInput(attrs={
#                 'class' : 'form-control'    
#             }),
#         }