import pandas as pd
import streamlit as st


# Using object notation
ip_floor= 5
ip_pitfloor = 2
ip_max_terminal = 5
ip_main_contactors_mode=2 # 2 or 4 
   
 #streamlit run "C:/Users/Amol/Desktop/Desktop Folder/streamlitexamplesnew/CodingPython/20230310-105542 - Copy.py"                                                      
system_configuration= []
global listToStr

def cal_system_config():
    global listToStr
    for i in range(ip_floor):
        if i<ip_floor-1:
            system_configuration.insert(0,ip_max_terminal-1)
        else:    
            system_configuration.insert(0,ip_max_terminal)
    listToStr = ' '.join([str(elem) for elem in system_configuration])


sy = []   
def cal_floorterminal():
    for i in range(len(system_configuration)):
        #print(i)
        if i == 0:
            list0 = []
            for j in range(system_configuration[i]):
                a = str("G"+str(j+1))
                list0.append(a)
            sy.append(list0)
        else:
            list0 = []
            for j in range(system_configuration[i]):
                a = str(str(i)+str(j+1))
                list0.append(a)
            sy.append(list0)
            listToStr = ' '.join([str(elem) for elem in sy])
           
list1 = []
list2 = []
def pitcal():
    global listToStr

    if ip_pitfloor == 1:
        for i in range(ip_max_terminal):
            a="P1"+str(i+1)
            list1.append(a)
            #print(list1)
    else:
        for i in range(ip_max_terminal):
            a="P1"+str(i+1)
            list1.append(a)
            #print(list1)

        for i in range(ip_max_terminal):
            a="P2"+str(i+1)
            list2.append(a)
            #print(list2)
finalsys = []
def drawsys():
    global finalsys
    if ip_pitfloor == 1:
        sy.append(list1)
    else:
        sy.append(list1)
        sy.append(list2)
    finalsys = sy 
    #print("bjasbj", finalsys)
   
    listToStr = ' '.join([str(elem) for elem in sy])
    #print(listToStr)
    #print(len(sy))
    for i in range(len(sy)):
        listToStr = ' '.join([str(elem) for elem in sy[i]])
        print(listToStr)
        st.text(listToStr)

cal_system_config()
#st.write("System Configuration List", system_configuration)
system_configuration.reverse() 
    #st.write("System Configuration Reverse List", system_configuration)
cal_floorterminal()
sy.reverse()
listToStr = ''.join([str(elem) for elem in sy])
    #st.write(listToStr)
pitcal()
drawsys()


print("final", finalsys)    
print("length of final sys", len(finalsys))

#finalsys = []
for i in range(len(finalsys)):
    a=finalsys[i]
    print(a)
    for j in a:
        print(j)
       
        
final_ud_list = []        
def ud_contactors(): 
    global final_ud_list   
    ud_k = (ip_floor-1)
    print(finalsys[0:ud_k])
    print(len(finalsys[0:ud_k]))
    final_ud_list = finalsys[0:ud_k] 
    print("final ud list", final_ud_list)
    count = 0
    for listElem in finalsys[0:4]:
        count += len(listElem)                            
        
        
    print("ud contactor no.", count)
ud_contactors()   


final_lr_list = []  
def lr_contactors():
    global final_lr_list
    lr_k= (ip_floor-1)
    print(lr_k)
    print(finalsys[1:(lr_k+1)])
    final_lr_list = finalsys[1:(lr_k+1)]
    print("final lr list", final_lr_list)
    count = 0
    for listElem in finalsys[1:(lr_k+1)]:
        count += len(listElem)
    print("lr contactor no.", count)
    
lr_contactors()


def main_contactors():
    if ip_main_contactors_mode==2:
        main_k=2
    else:    
        main_k=((ip_floor-1)*2)+2
        
    print("main k", main_k)
    
main_contactors()


final_ud_list1 = []  

def udinput():
    for i in range(len(final_ud_list)):
        global final_ud_list1
        a=final_ud_list[i]
        print(a)
        for j in a:
            print("jjjjjj",j)
            final_ud_list1.append(j)          

udinput()   


final_lr_list1 = [] 
def lrinput():
    for i in range(len(final_lr_list)):
        global final_lr_list1
        a=final_lr_list[i]
        print(a)
        for j in a:
            print("jjjjjj",j)
            final_lr_list1.append(j) 
lrinput()


print("final ud input", final_ud_list1) 
print("final lr input", final_lr_list1) 


df_ud = pd.DataFrame(final_ud_list1)
print(df_ud)

df_lr = pd.DataFrame(final_lr_list1)
print(df_lr)

df_rt = pd.DataFrame(final_lr_list1)
print(df_rt)

df_ud[0] = 'hls ' + df_ud[0].astype(str)
print(df_ud)

df_lr[0] = 'lf ' + df_lr[0].astype(str)
print(df_lr)
#df_rt = df_lr[[0]].copy()

df_rt[0] = 'rt ' + df_rt[0].astype(str)


col1, col2, col3 = st.columns(3)
with col1:
    st.dataframe(df_ud,300,500)

with col2:
    st.dataframe(df_lr,300,500)


frames = [df_ud, df_lr, df_rt]
print(frames)


result = pd.concat(frames,axis=1)
print(result)    
result.to_excel("output.xlsx",
             sheet_name='Sheet_name_1',header=False,index=False,startrow=10, startcol=10,index_label="HLS")  
#s_copy = df_lr.copy()
print(df_rt)