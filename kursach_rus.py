#Import Time
import time


Vehicle_Number=['XXXX-XX-XXXX']
Vehicle_Type=['Bike']
vehicle_Name=['Intruder']
Owner_Name=['Unknown']
Date=['22-22-3636']
Time=['22:22:22']
bikes=100
cars=250
bicycles=78
def main():
    global bikes,cars,bicycles
    try:
        while True:
            print("----------------------------------------------------------------------------------------")
            print("\t\t Менеджмент парковочных мест")
            print("----------------------------------------------------------------------------------------")
            print("1.Вьезд")
            print("2.Выезд" )
            print("3.Показать время парковки ")
            print("4.Просмотр парковочного места ")
            print("5.Информация о сумме ")
            print("6.Счет")
            print("7.Закрыть программу ")
            print("+---------------------------------------------+")
            ch=int(input("\tВыбрать опции:"))
            if ch==1:
                no=True
                while no==True:
                    Vno=input("\tВведите номер машины (XXXX-XX-XXXX) - ").upper()
                    if Vno=="":
                        print("###### Enter Vehicle No. ######")
                    elif Vno in Vehicle_Number:
                        print("###### Vehicle Number Already Exists")
                    elif len(Vno)==12:
                        no=not True
                        Vehicle_Number.append(Vno)
                    else:
                        print("###### Введите правильный номер машины ######")
                typee=True
                while typee==True:
                    Vtype=str(input("\tТип транспортного средства(Велосипед=A/Мотоцикл=B/Автомобиль=C):")).lower()
                    if Vtype=="":
                        print("###### Введите верный тип ######")
                    elif Vtype=="a":
                        Vehicle_Type.append("Bicycle")
                        bicycles-=1
                        typee=not True
                    elif Vtype=="b":
                        Vehicle_Type.append("Bike")
                        bikes-=1
                        typee=not True
                    elif Vtype=="c":
                        Vehicle_Type.append("Car")
                        cars-=1
                        typee=not True
                    else:
                        print("###### Пожалуйста введите верные опции ######")
                name=True
                while name==True:
                    vname=input("\tВведите название машины - ")
                    if vname=="":
                        print("########Пожалуйста введите название машины ########")
                    else:
                        vehicle_Name.append(vname)
                        name=not True
                o=True
                while o==True:
                    OName=input("\tИмя владельца - ")
                    if OName=="":
                        print("###### Пожалуйста введите имя владельца ######")
                    else:
                        Owner_Name.append(OName)
                        o=not True
                d=True
                while d==True:
                    date=input("\tВведите дату (DD-MM-YYYY) - ")
                    if date=="":
                        print("###### Введите дату ######")
                    elif len(date)!=10:
                        print("###### Введите верную дату ######")
                    else:
                        Date.append(date)
                        d=not True
                t=True
                while t==True:
                    time=input("\tВведите время (HH:MM:SS) - ")
                    if t=="":
                        print("###### Введите время ######")
                    elif len(time)!=8:
                        print("###### Пожалуйста введите верное время  ######")
                    else:
                        Time.append(time)
                        t=not True
                print("\n............................................................Запись деталей сохранена..................................................................")
            elif ch==2:
                no=True
                while no==True:
                    Vno=input("\tВведите номер для удаления(XXXX-XX-XXXX) - ").upper()
                    if Vno=="":
                        print("###### Enter No. ######")
                    elif len(Vno)==12:
                        if Vno in Vehicle_Number:
                            i=Vehicle_Number.index(Vno)
                            Vehicle_Number.pop(i)
                            Vehicle_Type.pop(i)
                            vehicle_Name.pop(i)
                            Owner_Name.pop(i)
                            Date.pop(i)
                            Time.pop(i)
                            no=not True
                            print("\n............................................................Удалено полностью..................................................................")
                        elif Vno not in Vehicle_Number:
                            print("###### Такой записи нет  ######")
                        else:
                            print("Ошибка")
                    else:
                        print("###### Введите правильный номер ######")
            elif ch==3:
                count=0
                print("----------------------------------------------------------------------------------------------------------------------")
                print("\t\t\t\tParked Vehicle")
                print("----------------------------------------------------------------------------------------------------------------------")
                print("Vehicle No.\tVehicle Type        Vehicle Name\t       Owner Name\t     Date\t\tTime")
                print("----------------------------------------------------------------------------------------------------------------------")
                for i in range(len(Vehicle_Number)):
                    count+=1
                    print(Vehicle_Number[i],"\t  ",Vehicle_Type[i],"\t            ",vehicle_Name[i],"\t       ",Owner_Name[i],"      " ,Date[i],"          ",Time[i])
                print("----------------------------------------------------------------------------------------------------------------------")
                print("------------------------------------------ Total Records - ",count,"-------------------------------------------------------")
                print("----------------------------------------------------------------------------------------------------------------------")
            elif ch==4:
                print("----------------------------------------------------------------------------------------------------------------------")
                print("\t\t\t\tSpaces Left For Parking")
                print("----------------------------------------------------------------------------------------------------------------------")
                print("\tSpaces Available for Bicycle - ",bicycles)
                print("\tSpaces Available for Bike - ",bikes)
                print("\tSpaces Available for Car - ",cars)
                print("----------------------------------------------------------------------------------------------------------------------")
            elif ch==5:
                print("----------------------------------------------------------------------------------------------------------------------")
                print("\t\t\t\tParking Rate")
                print("----------------------------------------------------------------------------------------------------------------------")
                print("*1.Bicycle      Rs20 / Hour")
                print("*2.Bike         Rs40/ Hour")
                print("*3.Car          Rs60/ Hour")
                print("----------------------------------------------------------------------------------------------------------------------")
            elif ch==6:
                print(".............................................................. Generating Bill ..........................................................................")
                no=True
                while no==True:
                    Vno=input("\tВведите номер машины для удаления(XXXX-XX-XXXX) - ").upper()
                    if Vno=="":
                        print("###### Введите номер ######")
                    elif len(Vno)==12:
                        if Vno in Vehicle_Number:
                            i=Vehicle_Number.index(Vno)
                            no=not True
                        elif Vno not in Vehicle_Number:
                            print("###### Такой записи нет ######")
                        else:
                            print("Ошибка")
                    else:
                        print("###### Введите правильный номер ######")
                print("\tВремя заезда - ",Time[i])
                print("\tДата заезда - ",Date[i])
                print("\tТип транспортного средства - ",Vehicle_Type[i])
                inp=True
                amt=0
                while inp==True:
                    hr=input("\tКоличество часов парковки - ").lower()
                    if hr=="":
                        print("###### Пожалуйста введите часы ######")
                    elif int(hr)==0 and Vehicle_Type[i]=="Bicycle":
                        amt=20
                        inp=not True
                    elif int(hr)==0 and Vehicle_Type[i]=="Bike":
                        amt=40
                        inp=not True
                    elif int(hr)==0 and Vehicle_Type[i]=="Car":
                        amt=60
                        inp=not True
                    elif int(hr)>=1:
                        if Vehicle_Type[i]=="Bicycle":
                            amt=int(hr)*int(20)
                            inp=not True
                        elif Vehicle_Type[i]=="Bike":
                            amt=int(hr)*int(40)
                            inp=not True
                        elif Vehicle_Type[i]=="Car":
                            amt=int(hr)*int(60)
                            inp=not True
                print("\t Начисление парковки - ",amt)
                ac=18/100*int(amt)
                print("\tдобавить 18 % - ",ac)
                print("\tОбщее начисление - ",int(amt)+int(ac))
                print("..............................................................Спасибо, что пользовались нашим сервисом1...........................................................................")
                a=input("\tНажмите любую клавишу, что бы продолжить - ")
            elif ch==7:
                print("..............................................................Спасибо, что пользовались сервисом!...........................................................................")
                print("                                     **********(: До встречи! :)**********")
                break
                quit
    except:
        main()
main()

