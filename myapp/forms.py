from django import forms

# pilihan
PIL = [
    (0, 'Perempuan'),
    (1, 'Laki - Laki'),
]

PILIHAN = [
    (1, 'Ya'),
    (0, 'Tidak'),
]

class Fomrdata(forms.Form):
	

    # year_in_school = models.CharField(
    #     max_length=2,
    #     choices=YEAR_IN_SCHOOL_CHOICES,
    #     default=FRESHMAN,
    # )

	jk = forms.ChoiceField(
		label='Jenis Kelamin',
		# max_length=3,
		choices=PIL,
		# default=1,
	)
	p_mengulang = forms.ChoiceField(choices=PILIHAN, label='Pernah Mengulan')
	ipk = forms.FloatField(label='IPK')
	p_cuti = forms.ChoiceField(choices=PILIHAN, label='Pernah Cuti')
	sam_bekerja = forms.ChoiceField(choices=PILIHAN, label='Sambil Bekerja')
	a_papua	= forms.ChoiceField(choices=PILIHAN, label='Asli Papua')
	ipk_sm1 = forms.FloatField(label='IPK Semester 1')