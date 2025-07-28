from django.db import models

class CallData(models.Model):
    name = models.CharField(max_length=255,unique=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    photo_hash = models.CharField(max_length=32, blank=True, null=True)
    bl = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    mark = models.DecimalField(max_digits=5, decimal_places=1,null=True)

    code1 = models.CharField(max_length=50, blank=True)
    code2 = models.CharField(max_length=50, blank=True)
    code3 = models.CharField(max_length=50, blank=True)
    code4 = models.CharField(max_length=50, blank=True)
    code5 = models.CharField(max_length=50, blank=True)
    code6 = models.CharField(max_length=50, blank=True)
    code7 = models.CharField(max_length=50, blank=True)
    code8 = models.CharField(max_length=50, blank=True)
    code9 = models.CharField(max_length=50, blank=True)
    code10 = models.CharField(max_length=50, blank=True)

    call1 = models.CharField(max_length=50, blank=True)
    call2 = models.CharField(max_length=50, blank=True)
    call3 = models.CharField(max_length=50, blank=True)
    call4 = models.CharField(max_length=50, blank=True)
    call5 = models.CharField(max_length=50, blank=True)
    call6 = models.CharField(max_length=50, blank=True)
    call7 = models.CharField(max_length=50, blank=True)
    call8 = models.CharField(max_length=50, blank=True)
    call9 = models.CharField(max_length=50, blank=True)
    call10 = models.CharField(max_length=50, blank=True)

    # Услуги
    service1 = models.CharField(max_length=100, blank=True)
    service2 = models.CharField(max_length=100, blank=True)
    service3 = models.CharField(max_length=100, blank=True)
    service4 = models.CharField(max_length=100, blank=True)
    service5 = models.CharField(max_length=100, blank=True)
    service6 = models.CharField(max_length=100, blank=True)
    service7 = models.CharField(max_length=100, blank=True)
    service8 = models.CharField(max_length=100, blank=True)
    service9 = models.CharField(max_length=100, blank=True)
    service10 = models.CharField(max_length=100, blank=True)

    # Приветствие
    greeting1 = models.IntegerField(null=True,blank=True)
    greeting2 = models.IntegerField(null=True,blank=True)
    greeting3 = models.IntegerField(null=True,blank=True)
    greeting4 = models.IntegerField(null=True,blank=True)
    greeting5 = models.IntegerField(null=True,blank=True)
    greeting6 = models.IntegerField(null=True,blank=True)
    greeting7 = models.IntegerField(null=True,blank=True)
    greeting8 = models.IntegerField(null=True,blank=True)
    greeting9 = models.IntegerField(null=True,blank=True)
    greeting10 = models.IntegerField(null=True,blank=True)



    hearing1 = models.IntegerField(null=True,blank=True)
    hearing2 = models.IntegerField(null=True,blank=True)
    hearing3 = models.IntegerField(null=True,blank=True)
    hearing4 = models.IntegerField(null=True,blank=True)
    hearing5 = models.IntegerField(null=True,blank=True)
    hearing6 = models.IntegerField(null=True,blank=True)
    hearing7 = models.IntegerField(null=True,blank=True)
    hearing8 = models.IntegerField(null=True,blank=True)
    hearing9 = models.IntegerField(null=True,blank=True)
    hearing10 = models.IntegerField(null=True,blank=True)

    question1 = models.IntegerField(null=True,blank=True)
    question2 = models.IntegerField(null=True,blank=True)
    question3 = models.IntegerField(null=True,blank=True)
    question4 = models.IntegerField(null=True,blank=True)
    question5 = models.IntegerField(null=True,blank=True)
    question6 = models.IntegerField(null=True,blank=True)
    question7 = models.IntegerField(null=True,blank=True)
    question8 = models.IntegerField(null=True,blank=True)
    question9 = models.IntegerField(null=True,blank=True)
    question10 = models.IntegerField(null=True,blank=True)

    interest1 = models.IntegerField(null=True,blank=True)
    interest2 = models.IntegerField(null=True,blank=True)
    interest3 = models.IntegerField(null=True,blank=True)
    interest4 = models.IntegerField(null=True,blank=True)
    interest5 = models.IntegerField(null=True,blank=True)
    interest6 = models.IntegerField(null=True,blank=True)
    interest7 = models.IntegerField(null=True,blank=True)
    interest8 = models.IntegerField(null=True,blank=True)
    interest9 = models.IntegerField(null=True,blank=True)
    interest10 = models.IntegerField(null=True,blank=True)

    cons1 = models.IntegerField(null=True,blank=True)
    cons2 = models.IntegerField(null=True,blank=True)
    cons3 = models.IntegerField(null=True,blank=True)
    cons4 = models.IntegerField(null=True,blank=True)
    cons5 = models.IntegerField(null=True,blank=True)
    cons6 = models.IntegerField(null=True,blank=True)
    cons7 = models.IntegerField(null=True,blank=True)
    cons8 = models.IntegerField(null=True,blank=True)
    cons9 = models.IntegerField(null=True,blank=True)
    cons10 = models.IntegerField(null=True,blank=True)

    polite1 = models.IntegerField(null=True,blank=True)
    polite2 = models.IntegerField(null=True,blank=True)
    polite3 = models.IntegerField(null=True,blank=True)
    polite4 = models.IntegerField(null=True,blank=True)
    polite5 = models.IntegerField(null=True,blank=True)
    polite6 = models.IntegerField(null=True,blank=True)
    polite7 = models.IntegerField(null=True,blank=True)
    polite8 = models.IntegerField(null=True,blank=True)
    polite9 = models.IntegerField(null=True,blank=True)
    polite10 = models.IntegerField(null=True,blank=True)

    speech1 = models.IntegerField(null=True,blank=True)
    speech2 = models.IntegerField(null=True,blank=True)
    speech3 = models.IntegerField(null=True,blank=True)
    speech4 = models.IntegerField(null=True,blank=True)
    speech5 = models.IntegerField(null=True,blank=True)
    speech6 = models.IntegerField(null=True,blank=True)
    speech7 = models.IntegerField(null=True,blank=True)
    speech8 = models.IntegerField(null=True,blank=True)
    speech9 = models.IntegerField(null=True,blank=True)
    speech10 = models.IntegerField(null=True,blank=True)

    note1 = models.IntegerField(null=True,blank=True)
    note2 = models.IntegerField(null=True,blank=True)
    note3 = models.IntegerField(null=True,blank=True)
    note4 = models.IntegerField(null=True,blank=True)
    note5 = models.IntegerField(null=True,blank=True)
    note6 = models.IntegerField(null=True,blank=True)
    note7 = models.IntegerField(null=True,blank=True)
    note8 = models.IntegerField(null=True,blank=True)
    note9 = models.IntegerField(null=True,blank=True)
    note10 = models.IntegerField(null=True,blank=True)

    warning1 = models.IntegerField(null=True,blank=True)
    warning2 = models.IntegerField(null=True,blank=True)
    warning3 = models.IntegerField(null=True,blank=True)
    warning4 = models.IntegerField(null=True,blank=True)
    warning5 = models.IntegerField(null=True,blank=True)
    warning6 = models.IntegerField(null=True,blank=True)
    warning7 = models.IntegerField(null=True,blank=True)
    warning8 = models.IntegerField(null=True,blank=True)
    warning9 = models.IntegerField(null=True,blank=True)
    warning10 = models.IntegerField(null=True,blank=True)

    emotion1 = models.IntegerField(null=True,blank=True)
    emotion2 = models.IntegerField(null=True,blank=True)
    emotion3 = models.IntegerField(null=True,blank=True)
    emotion4 = models.IntegerField(null=True,blank=True)
    emotion5 = models.IntegerField(null=True,blank=True)
    emotion6 = models.IntegerField(null=True,blank=True)
    emotion7 = models.IntegerField(null=True,blank=True)
    emotion8 = models.IntegerField(null=True,blank=True)
    emotion9 = models.IntegerField(null=True,blank=True)
    emotion10 = models.IntegerField(null=True,blank=True)

    solution1 = models.IntegerField(null=True,blank=True)
    solution2 = models.IntegerField(null=True,blank=True)
    solution3 = models.IntegerField(null=True,blank=True)
    solution4 = models.IntegerField(null=True,blank=True)
    solution5 = models.IntegerField(null=True,blank=True)
    solution6 = models.IntegerField(null=True,blank=True)
    solution7 = models.IntegerField(null=True,blank=True)
    solution8 = models.IntegerField(null=True,blank=True)
    solution9 = models.IntegerField(null=True,blank=True)
    solution10 = models.IntegerField(null=True,blank=True)

    dialog1 = models.DecimalField(max_digits=4,decimal_places=1,null=True)
    dialog2 = models.DecimalField(max_digits=4,decimal_places=1,null=True)
    dialog3 = models.DecimalField(max_digits=4,decimal_places=1,null=True)
    dialog4 = models.DecimalField(max_digits=4,decimal_places=1,null=True)
    dialog5 = models.DecimalField(max_digits=4,decimal_places=1,null=True)
    dialog6 = models.DecimalField(max_digits=4,decimal_places=1,null=True)
    dialog7 = models.DecimalField(max_digits=4,decimal_places=1,null=True)
    dialog8 = models.DecimalField(max_digits=4,decimal_places=1,null=True)
    dialog9 = models.DecimalField(max_digits=4,decimal_places=1,null=True)
    dialog10 = models.DecimalField(max_digits=4,decimal_places=1,null=True)


    comment1 = models.TextField(blank=True)
    comment2 = models.TextField(blank=True)
    comment3 = models.TextField(blank=True)
    comment4 = models.TextField(blank=True)
    comment5 = models.TextField(blank=True)
    comment6 = models.TextField(blank=True)
    comment7 = models.TextField(blank=True)
    comment8 = models.TextField(blank=True)
    comment9 = models.TextField(blank=True)
    comment10 = models.TextField(blank=True)

    mis1 = models.IntegerField(null=True,blank=True)
    mis2 = models.IntegerField(null=True,blank=True)
    mis3 = models.IntegerField(null=True,blank=True)

    month = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Текущий месяц ga '
        verbose_name_plural = 'Текущий месяц'

class ScoresForMonth(models.Model):
    operator = models.ForeignKey(CallData,on_delete=models.CASCADE,related_name='scores_for_month')
    month = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=255,null=True)
    group = models.CharField(max_length=255,null=True)
    mark = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    bl = models.CharField(max_length=255)
    code1 = models.CharField(max_length=50, blank=True)
    code2 = models.CharField(max_length=50, blank=True)
    code3 = models.CharField(max_length=50, blank=True)
    code4 = models.CharField(max_length=50, blank=True)
    code5 = models.CharField(max_length=50, blank=True)
    code6 = models.CharField(max_length=50, blank=True)
    code7 = models.CharField(max_length=50, blank=True)
    code8 = models.CharField(max_length=50, blank=True)
    code9 = models.CharField(max_length=50, blank=True)
    code10 = models.CharField(max_length=50, blank=True)

    call1 = models.CharField(max_length=50, blank=True)
    call2 = models.CharField(max_length=50, blank=True)
    call3 = models.CharField(max_length=50, blank=True)
    call4 = models.CharField(max_length=50, blank=True)
    call5 = models.CharField(max_length=50, blank=True)
    call6 = models.CharField(max_length=50, blank=True)
    call7 = models.CharField(max_length=50, blank=True)
    call8 = models.CharField(max_length=50, blank=True)
    call9 = models.CharField(max_length=50, blank=True)
    call10 = models.CharField(max_length=50, blank=True)

    # Услуги
    service1 = models.CharField(max_length=100, blank=True)
    service2 = models.CharField(max_length=100, blank=True)
    service3 = models.CharField(max_length=100, blank=True)
    service4 = models.CharField(max_length=100, blank=True)
    service5 = models.CharField(max_length=100, blank=True)
    service6 = models.CharField(max_length=100, blank=True)
    service7 = models.CharField(max_length=100, blank=True)
    service8 = models.CharField(max_length=100, blank=True)
    service9 = models.CharField(max_length=100, blank=True)
    service10 = models.CharField(max_length=100, blank=True)

    # Приветствие
    greeting1 = models.IntegerField(null=True, blank=True)
    greeting2 = models.IntegerField(null=True, blank=True)
    greeting3 = models.IntegerField(null=True, blank=True)
    greeting4 = models.IntegerField(null=True, blank=True)
    greeting5 = models.IntegerField(null=True, blank=True)
    greeting6 = models.IntegerField(null=True, blank=True)
    greeting7 = models.IntegerField(null=True, blank=True)
    greeting8 = models.IntegerField(null=True, blank=True)
    greeting9 = models.IntegerField(null=True, blank=True)
    greeting10 = models.IntegerField(null=True, blank=True)

    hearing1 = models.IntegerField(null=True, blank=True)
    hearing2 = models.IntegerField(null=True, blank=True)
    hearing3 = models.IntegerField(null=True, blank=True)
    hearing4 = models.IntegerField(null=True, blank=True)
    hearing5 = models.IntegerField(null=True, blank=True)
    hearing6 = models.IntegerField(null=True, blank=True)
    hearing7 = models.IntegerField(null=True, blank=True)
    hearing8 = models.IntegerField(null=True, blank=True)
    hearing9 = models.IntegerField(null=True, blank=True)
    hearing10 = models.IntegerField(null=True, blank=True)

    question1 = models.IntegerField(null=True, blank=True)
    question2 = models.IntegerField(null=True, blank=True)
    question3 = models.IntegerField(null=True, blank=True)
    question4 = models.IntegerField(null=True, blank=True)
    question5 = models.IntegerField(null=True, blank=True)
    question6 = models.IntegerField(null=True, blank=True)
    question7 = models.IntegerField(null=True, blank=True)
    question8 = models.IntegerField(null=True, blank=True)
    question9 = models.IntegerField(null=True, blank=True)
    question10 = models.IntegerField(null=True, blank=True)

    interest1 = models.IntegerField(null=True, blank=True)
    interest2 = models.IntegerField(null=True, blank=True)
    interest3 = models.IntegerField(null=True, blank=True)
    interest4 = models.IntegerField(null=True, blank=True)
    interest5 = models.IntegerField(null=True, blank=True)
    interest6 = models.IntegerField(null=True, blank=True)
    interest7 = models.IntegerField(null=True, blank=True)
    interest8 = models.IntegerField(null=True, blank=True)
    interest9 = models.IntegerField(null=True, blank=True)
    interest10 = models.IntegerField(null=True, blank=True)

    cons1 = models.IntegerField(null=True, blank=True)
    cons2 = models.IntegerField(null=True, blank=True)
    cons3 = models.IntegerField(null=True, blank=True)
    cons4 = models.IntegerField(null=True, blank=True)
    cons5 = models.IntegerField(null=True, blank=True)
    cons6 = models.IntegerField(null=True, blank=True)
    cons7 = models.IntegerField(null=True, blank=True)
    cons8 = models.IntegerField(null=True, blank=True)
    cons9 = models.IntegerField(null=True, blank=True)
    cons10 = models.IntegerField(null=True, blank=True)

    polite1 = models.IntegerField(null=True, blank=True)
    polite2 = models.IntegerField(null=True, blank=True)
    polite3 = models.IntegerField(null=True, blank=True)
    polite4 = models.IntegerField(null=True, blank=True)
    polite5 = models.IntegerField(null=True, blank=True)
    polite6 = models.IntegerField(null=True, blank=True)
    polite7 = models.IntegerField(null=True, blank=True)
    polite8 = models.IntegerField(null=True, blank=True)
    polite9 = models.IntegerField(null=True, blank=True)
    polite10 = models.IntegerField(null=True, blank=True)

    speech1 = models.IntegerField(null=True, blank=True)
    speech2 = models.IntegerField(null=True, blank=True)
    speech3 = models.IntegerField(null=True, blank=True)
    speech4 = models.IntegerField(null=True, blank=True)
    speech5 = models.IntegerField(null=True, blank=True)
    speech6 = models.IntegerField(null=True, blank=True)
    speech7 = models.IntegerField(null=True, blank=True)
    speech8 = models.IntegerField(null=True, blank=True)
    speech9 = models.IntegerField(null=True, blank=True)
    speech10 = models.IntegerField(null=True, blank=True)

    note1 = models.IntegerField(null=True, blank=True)
    note2 = models.IntegerField(null=True, blank=True)
    note3 = models.IntegerField(null=True, blank=True)
    note4 = models.IntegerField(null=True, blank=True)
    note5 = models.IntegerField(null=True, blank=True)
    note6 = models.IntegerField(null=True, blank=True)
    note7 = models.IntegerField(null=True, blank=True)
    note8 = models.IntegerField(null=True, blank=True)
    note9 = models.IntegerField(null=True, blank=True)
    note10 = models.IntegerField(null=True, blank=True)

    warning1 = models.IntegerField(null=True, blank=True)
    warning2 = models.IntegerField(null=True, blank=True)
    warning3 = models.IntegerField(null=True, blank=True)
    warning4 = models.IntegerField(null=True, blank=True)
    warning5 = models.IntegerField(null=True, blank=True)
    warning6 = models.IntegerField(null=True, blank=True)
    warning7 = models.IntegerField(null=True, blank=True)
    warning8 = models.IntegerField(null=True, blank=True)
    warning9 = models.IntegerField(null=True, blank=True)
    warning10 = models.IntegerField(null=True, blank=True)

    emotion1 = models.IntegerField(null=True, blank=True)
    emotion2 = models.IntegerField(null=True, blank=True)
    emotion3 = models.IntegerField(null=True, blank=True)
    emotion4 = models.IntegerField(null=True, blank=True)
    emotion5 = models.IntegerField(null=True, blank=True)
    emotion6 = models.IntegerField(null=True, blank=True)
    emotion7 = models.IntegerField(null=True, blank=True)
    emotion8 = models.IntegerField(null=True, blank=True)
    emotion9 = models.IntegerField(null=True, blank=True)
    emotion10 = models.IntegerField(null=True, blank=True)

    solution1 = models.IntegerField(null=True, blank=True)
    solution2 = models.IntegerField(null=True, blank=True)
    solution3 = models.IntegerField(null=True, blank=True)
    solution4 = models.IntegerField(null=True, blank=True)
    solution5 = models.IntegerField(null=True, blank=True)
    solution6 = models.IntegerField(null=True, blank=True)
    solution7 = models.IntegerField(null=True, blank=True)
    solution8 = models.IntegerField(null=True, blank=True)
    solution9 = models.IntegerField(null=True, blank=True)
    solution10 = models.IntegerField(null=True, blank=True)

    dialog1 = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    dialog2 = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    dialog3 = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    dialog4 = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    dialog5 = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    dialog6 = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    dialog7 = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    dialog8 = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    dialog9 = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    dialog10 = models.DecimalField(max_digits=4, decimal_places=1, null=True)

    comment1 = models.TextField(blank=True)
    comment2 = models.TextField(blank=True)
    comment3 = models.TextField(blank=True)
    comment4 = models.TextField(blank=True)
    comment5 = models.TextField(blank=True)
    comment6 = models.TextField(blank=True)
    comment7 = models.TextField(blank=True)
    comment8 = models.TextField(blank=True)
    comment9 = models.TextField(blank=True)
    comment10 = models.TextField(blank=True)

    mis1 = models.IntegerField(null=True, blank=True)
    mis2 = models.IntegerField(null=True, blank=True)
    mis3 = models.IntegerField(null=True, blank=True)



    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Архив ga '
        verbose_name_plural = 'Архив'


GRAPHIC_CHOICES = [
    ('1000', 'График 1000'),
    ('1009', 'График 1009'),
    ('112', 'График 112'),
]

class Schedule(models.Model):
    code = models.CharField(max_length=10, choices=GRAPHIC_CHOICES)
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} — {self.title}"

    class Meta:
        verbose_name = 'График'
        verbose_name_plural = 'Графики'
        ordering = ['-created_at']

class Management(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='documents')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Начальство ga '
        verbose_name_plural = 'Начальство'

class BackgroundImage(models.Model):
    image = models.ImageField(upload_to='backgrounds/')
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Background #{self.pk}"
    



class Records(models.Model):
    operator = models.ForeignKey(CallData,on_delete=models.CASCADE,related_name='Records')
    call_code = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,)
    record = models.FileField(upload_to='records', blank=True, null=True)


