# coding=utf-8

from django.db import models


class User(models.Model):
     UserName = models.CharField(max_length=100, blank=False)
     DisplayName = models.CharField(max_length=100, blank=False)
     UserPassword = models.CharField(max_length=100, blank=False)
     IsEnable = models.BooleanField(null=False)
     Email = models.CharField(max_length=300, blank=True)

     def __unicode__(self):
          return self.UserName

class Task(models.Model):
     TaskName = models.CharField(max_length=500, blank=False)
     TaskDesc = models.TextField(blank=True)
     ExecuteStartDT = models.DateTimeField(blank=True)
     Creator = models.CharField(max_length=100, blank=False)
     CreateDT = models.DateTimeField(blank=False)
     ExecuteEndDT = models.DateTimeField(blank=True)
     Requester = models.CharField(max_length=100, blank=False)
     TaskNo = models.IntegerField(blank=False)
     TaskType = models.CharField(max_length=100, blank=False)
     ExpectedStartDT = models.DateTimeField(blank=False)
     ExpectedEndDT = models.DateTimeField(blank=False)
     TaskState = models.CharField(max_length=100, blank=False)
     ProductVersion = models.CharField(max_length=100, blank=True)
     ReportCC = models.CharField(max_length=500, blank=True)
     ReportSendTo = models.CharField(max_length=500, blank=True)
     TaskComment = models.TextField(blank=True)
     TaskPriority = models.CharField(max_length=100, blank=True)
     TaskImportance = models.CharField(max_length=100, blank=True)
     RequestType = models.CharField(max_length=100, blank=False)
     Assessment = models.CharField(max_length=100, blank=True)
     TaskOwner = models.ForeignKey(User, blank=False)

     def __unicode__(self):
          return self.TaskName


class Product(models.Model):
     ProductName = models.CharField(max_length=100, blank=False)
     ProductDesc = models.CharField(max_length=300, blank=True)
     HasWeb = models.BooleanField(null=False)
     HasAndroid = models.BooleanField(null=False)
     HasIOS = models.BooleanField(null=False)
     HasWindowsPhone = models.BooleanField(null=False)
     IsEnabled = models.BooleanField(null=False)

     def __unicode__(self):
          return self.ProductName

class ProductType(models.Model):
     ProductTypeName = models.CharField(max_length=100, blank=False)
     IsEnable = models.BooleanField(null=False)
     MailTo = models.CharField(max_length=500, blank=True)
     MailCC = models.CharField(max_length=500, blank=True)
     MailBCC = models.CharField(max_length=500, blank=True)
     MailTitle = models.CharField(max_length=500, blank=True)
     MailContent = models.TextField(blank=True)
     BugSystem = models.CharField(max_length=100, blank=True)
     ProductId = models.ForeignKey(Product, blank=False)

     def __unicode__(self):
          return self.ProductTypeName


class Module(models.Model):
     ModuleName = models.CharField(max_length=100, blank=False)
     ModuleDesc = models.CharField(max_length=3000, blank=True)
     IsEnable = models.BooleanField(null=False)
     Level = models.IntegerField(blank=False)
     TreePath = models.CharField(max_length=500, blank=False)
     OrderField = models.IntegerField(blank=False)
     TreeIdPath = models.CharField(max_length=4000, blank=True)
     LastUpdateTime = models.DateTimeField(blank=True)
     CreateTime = models.DateTimeField(blank=True)
     ParentModuleId = models.IntegerField(blank=False)
     ProductTypeId = models.ForeignKey(ProductType, blank=False)

     def __unicode__(self):
          return self.ModuleName


class TestCase(models.Model):
     TestCaseName = models.CharField(max_length=100, blank=False)
     CreateTime = models.DateTimeField(blank=False)
     Priority = models.CharField(max_length=50, blank=True)
     TestCaseNo = models.IntegerField(blank=False)
     TestCaseDesc = models.TextField(blank=False)
     IsEnable = models.BooleanField(null=False)
     Automated = models.BooleanField(null=False)
     Tags = models.CharField(max_length=2000, blank=True)
     Abstract = models.CharField(max_length=4000, blank=True)
     LastUpdateDT = models.DateTimeField(blank=True)
     LastUpdateBy = models.CharField(max_length=255, blank=True)
     Creator = models.CharField(max_length=100, blank=False)
     ModuleId = models.ForeignKey(Module, blank=False)

     def __unicode__(self):
          return self.TestCaseName

class TestCaseAtt(models.Model):
     OriginalFileName = models.CharField(max_length=500, blank=False)
     FileName = models.CharField(max_length=500, blank=False)
     FileSize = models.IntegerField(blank=False)
     UploadDT = models.DateTimeField(blank=False)
     UploadBy = models.CharField(max_length=255, blank=False)
     IsEnable = models.BooleanField(null=False)
     Description = models.CharField(max_length=4000, blank=True)
     TestCaseId = models.ForeignKey(TestCase, blank=False)

     def __unicode__(self):
          return self.OriginalFileName


class Bug(models.Model):
     IssueID = models.CharField(max_length=100, blank=False)
     BugTitle = models.CharField(max_length=300, blank=False)
     BugState = models.CharField(max_length=100, blank=False)
     BugAssignTo = models.CharField(max_length=100, blank=True)
     BugSystem = models.CharField(max_length=100, blank=False)
     ProjectAlias = models.CharField(max_length=100, blank=True)
     ProjectName = models.CharField(max_length=100, blank=True)
     Tracker = models.CharField(max_length=100, blank=True)
     Priority = models.CharField(max_length=100, blank=True)
     Author = models.CharField(max_length=100, blank=True)
     Description = models.TextField(blank=True)
     StartDT = models.DateTimeField(blank=True)
     CreateOn = models.DateTimeField(blank=True)
     UpdateOn = models.DateTimeField(blank=True)
     BugAssignToId = models.CharField(max_length=100, blank=True)
     AuthorId = models.CharField(max_length=100, blank=True)
     Severity = models.CharField(max_length=100, blank=True)
     ProductTypeId = models.ForeignKey(ProductType, blank=False)

     def __unicode__(self):
          return self.BugTitle

class TaskBug(models.Model):
     BugDescription = models.TextField(blank=True)
     IsOldBug = models.BooleanField(null=False)
     TaskId = models.ForeignKey(Task, blank=False)

     # def __unicode__(self):
     #      return self.TaskId

class Result(models.Model):
     ExecuteResult = models.CharField(max_length=50, blank=False)
     Owner = models.CharField(max_length=100, blank=True)
     ResultDesc = models.CharField(max_length=1000, blank=True)
     IsEnable = models.BooleanField(null=False)
     LogFile = models.TextField(blank=True)
     ExecuteDT = models.DateTimeField(blank=True)
     ProductName = models.CharField(max_length=255, blank=True)
     ProductTypeName = models.CharField(max_length=100, blank=True)
     TaskId = models.ForeignKey(Task, blank=False)

     def __unicode__(self):
          return self.ExecuteResult


class TestCaseBug(models.Model):
     TestCaseId = models.ForeignKey(TestCase, blank=False)

     # def __unicode__(self):
     #      return self.aaaaa

