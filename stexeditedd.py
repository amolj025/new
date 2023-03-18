import pandas as pd
import streamlit as st


# Using object notation
#ip_floor= 5
#ip_pitfloor = 2
#ip_max_terminal = 5
#ip_main_contactors_mode=4 # 2 or 4 

ip_floor= st.sidebar.number_input('Insert floor number',min_value=1, step=1,key="1")
st.sidebar.write('The floor number is ', ip_floor)

ip_pitfloor = st.sidebar.number_input('Insert pitfloor number',min_value=1, step=1,key="2")
st.sidebar.write('The pitfloor number is ', ip_pitfloor)

ip_max_terminal = st.sidebar.number_input('Insert max terminal number',min_value=1, step=1,key="3")
st.sidebar.write('The max terminal number is ', ip_max_terminal)

ip_main_contactors_mode = st.sidebar.number_input('Insert main contactors',min_value=1, step=1,key="4")
st.sidebar.write('The main contactors is ', ip_main_contactors_mode)

   
 #streamlit run "C:/Users/Amol/Desktop/Desktop Folder/streamlitexamplesnew/CodingPython/stexeditedd.py"                                                      
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




if st.button("click me"):
    st.write(cal_system_config())
#st.write("System Configuration List", system_configuration)
    system_configuration.reverse() 
    #st.write("System Configuration Reverse List", system_configuration)
    st.write(cal_floorterminal())
    sy.reverse()
    listToStr = ''.join([str(elem) for elem in sy])
    #st.write(listToStr)
    st.write(pitcal())
    st.write(drawsys())


    print("final", finalsys)    
    print("length of final sys", len(finalsys))
    #st.write("final", finalsys)  
    #st.write("length of final sys", len(finalsys))
    #finalsys = []
    for i in range(len(finalsys)):
        a=finalsys[i]
        #print(a)
        for j in a:
            pass
            #print(j)
        
        
    final_ud_list = []        
    def ud_contactors(): 
        global final_ud_list   
        ud_k = (ip_floor-1)
        #print(finalsys[0:ud_k])
        #print(len(finalsys[0:ud_k]))
        final_ud_list = finalsys[0:ud_k] 
        #print("final ud list", final_ud_list)
        count = 0
        for listElem in finalsys[0:4]:
            count += len(listElem)                            
            
            
        print("ud contactor no.", count)
    ud_contactors()   


    final_lr_list = []  
    def lr_contactors():
        global final_lr_list
        lr_k= (ip_floor-1)
        #print(lr_k)
        #print(finalsys[1:(lr_k+1)])
        final_lr_list = finalsys[1:(lr_k+1)]
        #print("final lr list", final_lr_list)
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


    final_pit_list =[]
    def pit_contactors():
        global final_pit_list
        pit_k= ip_max_terminal
        count=0
        if ip_pitfloor==2:
            print("000000000", finalsys[-2:])
            final_pit_list = finalsys[-2:]
            count=ip_max_terminal
        else:
            print("000000000", finalsys[-1])
            final_pit_list = finalsys[-1:]
            count=ip_max_terminal     
            print("pit contactor", count)
            print(final_pit_list)

    pit_contactors()


    final_ud_list1 = []  

    def udinput():
        for i in range(len(final_ud_list)):
            global final_ud_list1
            a=final_ud_list[i]
            #print(a)
            for j in a:
                #print("jjjjjj",j)
                final_ud_list1.append(j)          

    udinput()   


    final_lr_list1 = [] 
    def lrinput():
        for i in range(len(final_lr_list)):
            global final_lr_list1
            a=final_lr_list[i]
            #print(a)
            for j in a:
                #print("jjjjjj",j)
                final_lr_list1.append(j) 
    lrinput()

    final_pit_list1 = []
    final_pit_list2 = []
    def pitinput():
        print(final_pit_list)
        global final_pit_list1
        global final_pit_list2
        for i in range(len(final_pit_list)):
            a=final_pit_list[i]
            #print(a)
            for j in a:
                #print("jjjjjj",j)
                final_pit_list1.append(j)


        for i in range(ip_max_terminal):
            final_pit_list2.append(i+1)

    pitinput()  
             
    st.write(final_ud_list1)
    st.write(final_lr_list1)
    st.write(final_pit_list1)
    st.write(final_pit_list2)
    print("final ud input", final_ud_list1) 
    print("final lr input", final_lr_list1) 
    print("final pit input", final_pit_list1) 
    print("final pit input 2", final_pit_list2) 
    df_ud = pd.DataFrame(final_ud_list1)
        #print(df_ud)

    df_lr = pd.DataFrame(final_lr_list1)
        #print(df_lr)

    df_rt = pd.DataFrame(final_lr_list1)
        #print(df_rt)

    df_pit = pd.DataFrame(final_pit_list1)

    df_pit1 = pd.DataFrame(final_pit_list2)

    df_gls = pd.DataFrame(final_pit_list2)

    df_ud[0] = 'hls ' + df_ud[0].astype(str)
        #print(df_ud)

    df_lr[0] = 'lf ' + df_lr[0].astype(str)
        #print(df_lr)
        #df_rt = df_lr[[0]].copy()

    df_rt[0] = 'rt ' + df_rt[0].astype(str)

    df_pit[0] = 'gls ' + df_pit[0].astype(str)
    df_pit1[0] = 'hls P' + df_pit1[0].astype(str) 
    df_gls[0] = 'gls C' + df_gls[0].astype(str) 

    col1, col2, col3 = st.columns(3)
    with col1:
        st.dataframe(df_ud,300,500)

    with col2:
        st.dataframe(df_lr,300,500)


    frames = [df_ud, df_lr, df_rt,df_pit,df_pit1,df_gls]
        #print(frames)







    import io
    buffer = io.BytesIO()

    result = pd.concat(frames,axis=1)
    print(result)     
    print(type(result))
    re = result.to_csv(index=False,header=None)
        #re = result.to_excel("output.xlsx",
        #            sheet_name='Sheet_name_1',header=False,index=False,startrow=1, startcol=1,index_label="HLS")  
        #s_copy = df_lr.copy()
        #print(df_rt)

    st.download_button("Press to Download",re,"file.csv","text/csv")
