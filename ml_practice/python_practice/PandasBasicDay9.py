


import pandas as pd

survey_data = {
    "Respondent ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    "Age": [22, 35, 55, 68, 30, 45, 29, 63, 40, 24, 38, 50, 27, 19, 61],
    "Gender": ["Male", "Female", "Female", "Male", "Male", "Female", "Male", "Female", "Male", "Female", 
               "Female", "Male", "Male", "Female", "Male"],
    "State": ["California", "California", "Texas", "Texas", "New York", "Florida", "Florida", "New York",
              "California", "Texas", "Nevada", "Nevada", "California", "Texas", "Florida"],
    "Candidate": ["Candidate A", "Candidate B", "Candidate A", "Candidate C", "Candidate A", "Candidate B", 
                  "Candidate A", "Candidate C", "Candidate A", "Candidate B", "Candidate B", "Candidate A",
                  "Candidate C", "Candidate A", "Candidate B"],
    "Education": ["Bachelor's", "Master's", "High School", "High School", "Bachelor's", "PhD", "Bachelor's",
                  "Associate", "Master's", "Bachelor's", "Master's", "Bachelor's", "High School", "Bachelor's",
                  "PhD"],
    "Employment Status": ["Employed", "Employed", "Retired", "Retired", "Self-employed", "Employed", 
                          "Self-employed", "Retired", "Employed", "Student", "Employed", "Employed",
                          "Student", "Student", "Retired"]
}


df=pd.DataFrame(survey_data)
# print(df)



# updating row  /creating row

# df.iloc[4]=[1,2,3,4,5,6,7]
# df.iloc[4]=11111



#  update perticuler  value in database 
# df['Age'][0]=11

# rename dFcol

# df.rename(columns={"Gender":"type"},inplace=True)


# update column / add column

df['Name']=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]

# deleting column

df.pop("Name")


# accesing first 4 elements

# h4=df.head(4)
# print(h4)


# accesinng elements from last

# t4=df.tail(4)
# print(t4)

# row lables and loc accessing

row_lables=['f1',"f2","f3","f4","f5","f6","f7","f8","f9","f10","f11",'f12','f13','f14',"f15"]
df.index=row_lables
# a=df.columns.get_loc("Age")
# print(a)
# print(df.loc["f4"])
# print(df)