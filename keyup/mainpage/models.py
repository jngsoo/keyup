from django.db import models

class dummy_for_histo_and_cloud(models.Model):
    objects = models.Manager()
    # "id" serial NOT NULL PRIMARY KEY 자동 생성
    companies = (
        ('1', 'CNS'),
        ('2', '네이버'),
        ('3', 'SDS'),
        ('4', '쿠팡'),
        ('5', '구글'),
        ('6', '카카오'),
        ('7', '배민'),
        ('8', 'AWS'),
        ('9', 'C&C'),
        ('10', '퀄컴'),
    )
    company_name = models.CharField(max_length=100, choices=companies)
    # IoT, 머신러닝, 이런게 x축에 박힌다고 생각하고
    x_axis_keyword = models.CharField(max_length=50)
    # 빈도수가 정수형으로 박힌다고 생각하자
    y_axis_quantity = models.IntegerField()

    # 연관성 있는 키워드들
    related_keyword_1 = models.CharField(max_length=20, null=True, blank=True)
    related_keyword_2 = models.CharField(max_length=20, null=True, blank=True)
    related_keyword_4 = models.CharField(max_length=20, null=True, blank=True)
    related_keyword_5 = models.CharField(max_length=20, null=True, blank=True)
    related_keyword_3 = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.get_company_name_display() + " : " + self.x_axis_keyword + " " + str(self.y_axis_quantity)

class TimeGraph(models.Model):
    objects = models.Manager()
    dates = (
        ('1', '2018 1-3월'),
        ('2', '2018 4-6월'),
        ('3', '2018 7-9월'),
        ('4', '2018 10-12월'),
        ('5', '2019 1-3월'),
        ('6', '2019 4-6월'),
    )
    companies = (
        ('1', 'CNS'),
        ('2', '네이버'),
        ('3', 'SDS'),
        ('4', '쿠팡'),
        ('5', '구글'),
        ('6', '카카오'),
        ('7', '배민'),
        ('8', 'AWS'),
        ('9', 'C&C'),
        ('10', '퀄컴'),
    )
    time = models.CharField(max_length=2, choices=dates)
    company_name = models.CharField(max_length=100, choices=companies)
    x_axis_keyword = models.CharField(max_length=50)
    y_axis_quantity = models.IntegerField()


    def __str__(self):
        return self.time + " " + self.get_company_name_display() + " : " + self.x_axis_keyword +  " " + str(self.y_axis_quantity)



class histo_2(models.Model):
    objects = models.Manager()
    # "id" serial NOT NULL PRIMARY KEY 자동 생성
    companies = (
        ('1', 'CNS'),
        ('2', '네이버'),
        ('3', 'SDS'),
        ('4', '쿠팡'),
        ('5', '구글'),
        ('6', '카카오'),
        ('7', '배민'),
        ('8', 'AWS'),
        ('9', 'C&C'),
        ('10', '퀄컴'),
    )
    company_name = models.CharField(max_length=100, choices=companies)
    # IoT, 머신러닝, 이런게 x축에 박힌다고 생각하고
    x_axis_keyword = models.CharField(max_length=50)
    # 빈도수가 정수형으로 박힌다고 생각하자
    y_axis_quantity = models.IntegerField()

    # 연관성 있는 키워드들
    related_keyword_1 = models.CharField(max_length=20, null=True, blank=True)
    related_keyword_2 = models.CharField(max_length=20, null=True, blank=True)
    related_keyword_4 = models.CharField(max_length=20, null=True, blank=True)
    related_keyword_5 = models.CharField(max_length=20, null=True, blank=True)
    related_keyword_3 = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.get_company_name_display() + " : " + self.x_axis_keyword + " " + str(self.y_axis_quantity)






