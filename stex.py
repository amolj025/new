
import streamlit as st

# Using object notation
ip_floor= st.sidebar.number_input('Insert floor number',min_value=1, step=1,key="1")
st.sidebar.write('The floor number is ', ip_floor)

ip_pitfloor = st.sidebar.number_input('Insert pitfloor number',min_value=1, step=1,key="2")
st.sidebar.write('The pitfloor number is ', ip_pitfloor)

ip_max_terminal = st.sidebar.number_input('Insert max terminal number',min_value=1, step=1,key="3")
st.sidebar.write('The max terminal number is ', ip_max_terminal)


   
 #streamlit run "c:/Users/Amol/Desktop/Desktop Folder/streamlitexamplesnew/stex.py" 

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
        print(i)
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
            print(list1)
    else:
        for i in range(ip_max_terminal):
            a="P1"+str(i+1)
            list1.append(a)
            print(list1)

        for i in range(ip_max_terminal):
            a="P2"+str(i+1)
            list2.append(a)
            print(list2)
finalsys = []
def drawsys():
    if ip_pitfloor == 1:
        sy.append(list1)
    else:
        sy.append(list1)
        sy.append(list2)
    finalsys = sy 
    print("bjasbj", finalsys)
   
    listToStr = ' '.join([str(elem) for elem in sy])
    st.write(listToStr)
    print(len(sy))
    for i in range(len(sy)):
        listToStr = ' '.join([str(elem) for elem in sy[i]])
        st.write(listToStr)
        print(listToStr)

         


if st.button("click me"):
    st.write(cal_system_config())
    st.write("System Configuration String", listToStr)
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