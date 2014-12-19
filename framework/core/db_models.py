# coding=utf-8


def sql(tables_vals):
    list=[]
    for i in range(0,len(tables_vals)):
        k = tables_vals.keys()[i]
        v = tables_vals.values()[i]
        sql_str = 'create table if not exists %s (id integer primary key,%s)' % (k,v)
        list.append(sql_str)
    return list

def Tables():
    tables={}

    StressResult = '''
    Lable varchar(100) NOT NULL,
    Samples integer NULL,
    Average integer NULL,
    Median integer NULL,
    LineNinety  integer NULL,
    MinValue integer NULL,
    MaxValue integer NULL,
    ErrorRate integer NULL,
    Throughput integer NULL,
    Kbs integer NULL,
    Loop integer NOT NULL,
    StartupTime integer NOT NULL
    '''
    tables.setdefault('StressResult',StressResult)

    Product = '''
    ProductName varchar(100) NOT NULL,
    ProductDesc varchar(300) NULL,
    HasAndroid integer NOT NULL,
    HasInterface integer NOT NULL,
    HasIOS integer NOT NULL,
    HasWeb integer NOT NULL,
    HasWindowsPhone integer NOT NULL,
    IsEnabled integer NOT NULL
    '''
    tables.setdefault('Product',Product)

    ProductType = '''
    ProductCatName varchar(100) NOT NULL,
    ProductTypeName varchar(100) NOT NULL,
    IsEnable integer NOT NULL,
    Product_Id integer NOT NULL
    '''
    tables.setdefault('ProductType',ProductType)

    Module = '''
    ModuleName varchar(100) NOT NULL,
    ModuleDesc varchar(3000) NULL,
    IsEnable integer NOT NULL,
    Level integer NOT NULL,
    TreePath varchar(500) NOT NULL,
    OrderField integer NOT NULL,
    TreeIdPath varchar(4000) NULL,
    LastUpdateTime datetime NULL,
    CreateTime datetime NULL,
    ParentModuleId integer NOT NULL,
    ProductType_Id integer NOT NULL
    '''
    tables.setdefault('Module',Module)

    TestCase = '''
    TestCaseName varchar(100) NOT NULL,
    CreateTime datetime NOT NULL,
    Creator varchar(100) NOT NULL,
    Priority varchar(50) NULL,
    TestCaseNo integer NOT NULL,
    TestCaseDesc text NOT NULL,
    Script varchar(100) NULL,
    IsEnable integer NOT NULL,
    Automated integer NOT NULL,
    Tags varchar(2000) NULL,
    Abstract varchar(4000) NULL,
    LastUpdateDT datetime NULL,
    LastUpdateBy varchar(255) NULL
    '''
    tables.setdefault('TestCase',TestCase)

    TestCaseAtt = '''
    OriginalFileName varchar(500) NOT NULL,
    FileName varchar(500) NOT NULL,
    FileSize integer NOT NULL,
    UploadDT datetime NOT NULL,
    UploadBy varchar(255) NOT NULL,
    IsEnable integer NOT NULL,
    Description varchar(4000) NULL,
    TestCase_Id integer NOT NULL
    '''
    tables.setdefault('TestCaseAtt',TestCaseAtt)

    TestCaseDetail = '''
    Actual varchar(1000) NULL,
    Expectation varchar(1000) NULL,
    IsEnable integer NOT NULL,
    TestCase_Id integer NOT NULL,
    Module_Id integer NOT NULL
    '''
    tables.setdefault('TestCaseDetail',TestCaseDetail)
    
    Task = '''
	TaskName varchar(500) NOT NULL,
	TaskDescription text NULL,
	ExecuteStartDate datetime NULL,
	Creator varchar(100) NOT NULL,
	CreateDateTime datetime NOT NULL,
	ExecuteEndDate datetime NULL,
	Requester varchar(100) NOT NULL,
	TaskNo integer NOT NULL,
	TaskType varchar(100) NOT NULL,
	ExpectedStartDateTime datetime NOT NULL,
	ExpectedEndDateTime datetime NOT NULL,
	TaskState varchar(100) NOT NULL,
	ProductVersion varchar(100) NULL,
	ReportCC varchar(500) NULL,
	ReportSendTo varchar(500) NULL,
	TaskComment text NULL,
	TaskOwner integer NULL,
	TaskPriority varchar(100) NULL,
	TaskImportance varchar(100) NULL,
	RequestType varchar(100) NOT NULL,
	HardwareVersion varchar(100) NULL,
	Assessment varchar(100) NULL,
	ProductType_Id integer NOT NULL
	'''
    tables.setdefault('Task',Task)

    Bug = '''
    IssueID varchar(100) NOT NULL,
    BugTitle varchar(300) NOT NULL,
    BugState varchar(100) NOT NULL,
    BugAssignTo varchar(100) NULL,
    BugSystem varchar(100) NOT NULL,
    ProjectAlias varchar(100) NULL,
    ProjectName varchar(100) NULL,
    Tracker varchar(100) NULL,
    Priority varchar(100) NULL,
    Author varchar(100) NULL,
    Description text NULL,
    StartDT datetime NULL,
    CreateOn datetime NULL,
    UpdateOn datetime NULL,
    BugAssignToId varchar(100) NULL,
    AuthorId varchar(100) NULL,
    Severity varchar(100) NULL,
    ProductType_Id integer NOT NULL
    '''
    tables.setdefault('Bug',Bug)

    TaskBug = '''
    BugDescription text NULL,
    IsOldBug integer NOT NULL,
    Task_Id integer NOT NULL
    '''
    tables.setdefault('TaskBug',TaskBug)
    
    Context = '''
	ContextName varchar(100) NOT NULL,
	ContextType varchar(100) NULL,
	PCOS varchar(100) NULL,
	MobileOS varchar(100) NULL,
	PCWeb varchar(100) NULL,
	MobileWeb varchar(100) NULL,
	Description varchar(1000) NULL,
	ContextDisplayName varchar(500) NOT NULL
	'''
    tables.setdefault('Context',Context)

    Result = '''
    ExecuteResult varchar(50) NOT NULL,
    Owner varchar(100) NULL,
    ResultDesc varchar(1000) NULL,
    IsEnable integer NOT NULL,
    LogFile text NULL,
    ExecuteDT datetime NULL,
    ProductName varchar(255) NULL,
    ProductTypeName varchar(100) NULL,
	TestCase_Id integer NOT NULL,
	Context_Id integer NOT NULL,
    Task_Id integer NOT NULL
    '''
    tables.setdefault('Result',Result)

    TestCaseBug = '''
    TestCase_Id integer NOT NULL
    '''
    tables.setdefault('TestCaseBug',TestCaseBug)

    return tables
