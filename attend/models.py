from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subname(models.Model):
	sub1=models.CharField(max_length=200)
	sub2=models.CharField(max_length=200)
	sub3=models.CharField(max_length=200)
	sub4=models.CharField(max_length=200)
	sub5=models.CharField(max_length=200)
	sub6=models.CharField(max_length=200)
	tot1=models.IntegerField()
	tot2=models.IntegerField()
	tot3=models.IntegerField()
	tot4=models.IntegerField()
	tot5=models.IntegerField()
	tot6=models.IntegerField()
	att=models.IntegerField()
	# attendance_criteria=models.IntegerField()
# 	subs = ArrayField(models.CharField(max_length=10, blank=True),size=8)
# 	no_of_classes = ArrayField(models.IntegerField( blank=True),size=8)
	

	def __str__(self):
		return f"{self.sub1}| {self.sub2} | | {self.sub3}| {self.sub4}| {self.sub5}| {self.sub6}"
		# always return short things

# # class Comment(models.Model):
# # 	post=models.ForeignKey(BlogPost,on_delete=models.CASCADE)
# # 	text=models.TextField()
# # 	timestamp=models.DateTimeField(auto_now_add=True)
# # 	user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

# # 	def __str__(self):
# # 		return f"{self.post.title} | {self.text[:30]}"