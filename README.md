# Attrition_analytics
Project 'Analytics of working conditions impact on worker's attrition' (Innopolis University Specialized IT Training Center)

## Contents
- [Technologies](#Technologies)
- [Model Import](#Import)
- [Data describe](#Data)

## Technologies
- Python 3:
    - Pandas
    - Numpy
    - Scikit-learn
    - MatPlotLib
    - Pickle

 ## Import
 Python3 has to be installed
 1) Load file 'decisiontree.pickle'
 2) Open files 'decisiontree.pickle' and 'model_pickle.py' in your IDE
 3) Past your data's path into line 4 (It must be csv file; columns and types of data must be the same as the [original data](#Data) without column 'Attrition')
 4) Past 'decisiontree.pickle' path into line 6

## Data
 0   Age                                   int64
 
 1   DailyRate                             int64
 
 2   DistanceFromHome                      int64
 
 3   Education                             int64
 
 4   EmployeeNumber                        int64

 5   EnvironmentSatisfaction               int64
 
 6   HourlyRate                            int64
 
 7   JobInvolvement                        int64
 
 8   JobLevel                              int64
 
 9   JobSatisfaction                       int64
 
 10  MonthlyIncome                         int64
 
 11  MonthlyRate                           int64
 
 12  NumCompaniesWorked                    int64
 
 13  PercentSalaryHike                     int64
 
 14  RelationshipSatisfaction              int64
 
 15  StockOptionLevel                      int64
 
 16  TotalWorkingYears                     int64
 
 17  TrainingTimesLastYear                 int64
 
 18  WorkLifeBalance                       int64
 
 19  YearsAtCompany                        int64
 
 20  YearsInCurrentRole                    int64
 
 21  YearsSinceLastPromotion               int64
 
 22  YearsWithCurrManager                  int64
 
 23  Attrition_No                          bool 
 
 24  Attrition_Yes                         bool 
 
 25  BusinessTravel_Non-Travel             bool 
 
 26  BusinessTravel_Travel_Frequently      bool 
 
 27  BusinessTravel_Travel_Rarely          bool 
 
 28  Department_Human Resources            bool 
 
 29  Department_Research & Development     bool 
 
 30  Department_Sales                      bool 
 
 31  EducationField_Human Resources        bool 
 
 32  EducationField_Life Sciences          bool 
 
 33  EducationField_Marketing              bool 
 
 34  EducationField_Medical                bool 
 
 35  EducationField_Other                  bool 
 
 36  EducationField_Technical Degree       bool 
 
 37  Gender_Female                         bool 
 
 38  Gender_Male                           bool 
 
 39  JobRole_Healthcare Representative     bool 
 
 40  JobRole_Human Resources               bool 
 
 41  JobRole_Laboratory Technician         bool 
 
 42  JobRole_Manager                       bool 
 
 43  JobRole_Manufacturing Director        bool 
 
 44  JobRole_Research Director             bool 
 
 45  JobRole_Research Scientist            bool 
 
 46  JobRole_Sales Executive               bool 

 47  JobRole_Sales Representative          bool 
 
 48  MaritalStatus_Divorced                bool 
 
 49  MaritalStatus_Married                 bool 
 
 50  MaritalStatus_Single                  bool 
 
 51  OverTime_No                           bool 
 
 52  OverTime_Yes                          bool 
