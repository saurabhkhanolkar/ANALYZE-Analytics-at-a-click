import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 
import plotly.express as px
import missingno as msno 
import seaborn as sns



html_temp = """
    <div style="background-color:black ;padding:10px">
    <h1 style="color:white;text-align:center;">ANALYZE</h1>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)

html_temp69 = """
    <div style="background-color:white ;padding:10px">
    <h3 style="color:black;text-align:center;">PLEASE HAVE A LOOK AT THE SIDEBAR TO MAKE THE BEST USE OF ANALYZE.</h3>
    </div>
    """
st.markdown(html_temp69, unsafe_allow_html=True)

#st.markdown('<b>PLEASE HAVE A LOOK AT THE SIDEBAR TO MAKE THE BEST USE OF ANALYZE. </b>', unsafe_allow_html=True)




st.sidebar.header("ANALYSE DATA AT THE CLICK OF A BUTTON!")

st.sidebar.markdown('<b>ABOUT:</b>', unsafe_allow_html=True)
st.sidebar.markdown("EDA(Exploratory Data Analytics) and Data Preprocessing take up anywhere from 50% to 70 % of the total time, resources and energy spent on an Analytics project. Further on, it involves writing complex logic and convoluted pieces of code which is enough to drain the developer out. Meet, 'ANALYZE' ! ANALYZE allows you to perform this extremely painstaking and convoluted task of EDA at the click of a button! Hence saving you all the time, resources and energy! Now, analyse your data at only the click of a button!")
st.sidebar.markdown('<b>HOW DOES IT WORK?:</b>', unsafe_allow_html=True)  
st.sidebar.markdown("Upload a csv file of the structured dataset of the project you are currently working on and press 'Analyse'. 'ANALYZE' computes the following information for you:")
st.sidebar.markdown("1.Data Overview: A prima facie summary of your entire data.")
st.sidebar.markdown("2.Univariate Anaysis: An analysis of how individual variables are distributed.")
st.sidebar.markdown("3.Missing Value Analysis: An analysis of 'The Number of missing values per column' and the Visualization of 'The missing values in the dataset'") 
st.sidebar.markdown("4.Multivariate Analysis: A concise report that displays all the correlations in your data, in turn helping you manage multi collinearity and make informed decisions.")
st.sidebar.markdown('<b>CREATED BY:</b>', unsafe_allow_html=True)
st.sidebar.markdown('Saurabh Khanolkar')
st.sidebar.markdown('Email : saurabh.khanolkar@gmail.com')
st.sidebar.markdown('Linkedin : https://tinyurl.com/ybbegcs4')
st.sidebar.markdown('<b>HAPPY ANALYSING!</b>', unsafe_allow_html=True)  

uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"]) 
def upload():
    df1=pd.read_csv(uploaded_file)
    return(df1)
    
    
    


#1. determining the type of variable
def var_type(df):
    list1=[]
    for i in range(len(df.columns)):
        x=df.iloc[:,i]
        list1.append(np.issubdtype(x.dtype, np.number))
    return(list1)
    
#2.univariate analysis(look at the skewness then decide the imputation strategy... mean, median or mode)

def univariate(df):
    
    
    cs=list(df.columns)
    #numerical
    x=var_type(df)
    st.markdown('<b>Individual variables are distributed in the following manner:</b>', unsafe_allow_html=True)
    for i in range(len(x)):
        if(x[i]==True):
            fig = px.histogram(df.iloc[:,i])
            fig1 = px.box(df.iloc[:,i])
            st.header(i+1)
            st.markdown('<b>Variable:</b>', unsafe_allow_html=True)
            st.write(cs[i])
            st.plotly_chart(fig)
            st.plotly_chart(fig1)
    #categorical
        else:
            st.header(i+1)
            st.markdown('<b>Variable:</b>', unsafe_allow_html=True)
            st.write(cs[i])
            df46=df.iloc[:,i]
            fig3 = px.bar(df46)
            st.plotly_chart(fig3)
            
    
    
    
    
        



#3. handling missing values
def missing(df):
    #showcasing missing value
    plt.figure(figsize = (20,20))
    sns.set(font_scale=2)
    st.markdown('<b>Number of missing values per column:</b>', unsafe_allow_html=True)
    p=df.isnull().sum()
    st.write(p)
    st.markdown('<b>Visualizing the missing values in the dataset:</b>', unsafe_allow_html=True)
    st.write(msno.matrix(df)) 
    st.pyplot()
    #numerical
    
    
    
    #categorical


#4.multivariate Analysis(correlation heatmap,detecting multicollinearity)
def multivariate(df):
    corrMatrix = df.corr()
    st.markdown('<b>Correlation chart for the dataset:</b>', unsafe_allow_html=True)
    st.write(corrMatrix)
    
    
    
if st.button("Analyse"):
    
    df2=upload()
    html_temp2 = """
    <div style="background-color:black ;padding:10px">
    <h3 style="color:white;text-align:center;">OVERVIEW OF THE DATA</h3>
    </div>
    """
    
    st.markdown(html_temp2, unsafe_allow_html=True)

    
    list1=var_type(df2)
    cs=list(df2.columns)
    for i in range(len(list1)):
       
        if(list1[i]==0):
            st.header(i+1)
            st.markdown('<b>Column:</b>', unsafe_allow_html=True)
            st.write(cs[i])
            st.markdown('<b>Type:</b>', unsafe_allow_html=True)
            st.write( 'categorical variable')
            df45=df2.iloc[:,i]
            st.markdown('<b>Contingency Table:</b>', unsafe_allow_html=True)
            st.write(pd.DataFrame(df45.value_counts()))
         
            

            
        else:
            st.header(i+1)
            st.markdown('<b>Column:</b>', unsafe_allow_html=True)
            st.write(cs[i])
            st.markdown('<b>Type:</b>', unsafe_allow_html=True)
            st.write('numerical variable')
            st.markdown('<b>Mean:</b>', unsafe_allow_html=True)
            st.write(np.mean(df2.iloc[:,i]))
            st.markdown('<b>Min:</b>', unsafe_allow_html=True)
            st.write(np.min(df2.iloc[:,i]))
            st.markdown('<b>Max:</b>', unsafe_allow_html=True)
            st.write(np.max(df2.iloc[:,i]))
            st.markdown('<b>Standard Deviation:</b>', unsafe_allow_html=True)
            st.write(np.std(df2.iloc[:,i]))
    

    html_temp3 = """
    <div style="background-color:black ;padding:10px">
    <h3 style="color:white;text-align:center;">UNIVARIATE ANALYSIS</h3>
    </div>
    """
    
    st.markdown(html_temp3, unsafe_allow_html=True)
    univariate(df2)
    html_temp4 = """
    <div style="background-color:black ;padding:10px">
    <h3 style="color:white;text-align:center;">MISSING DATA ANALYSIS</h3>
    </div>
    """
    
    st.markdown(html_temp4, unsafe_allow_html=True)
    missing(df2)
    html_temp5 = """
    <div style="background-color:black ;padding:10px">
    <h3 style="color:white;text-align:center;">MULTIVARIATE ANALYSIS</h3>
    </div>
    """
    
    st.markdown(html_temp5, unsafe_allow_html=True)

    multivariate(df2)
    
