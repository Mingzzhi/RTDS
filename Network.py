# Imports
import os
import dss
import math
import time

start_time = time.time()

# # Set Path
# my_directory = os.getcwd()
# print(f"The direction is located in the following path: my_directory = {my_directory}")
#
# # Set up DSS
# dss_engine = dss.DSS
# DSSText = dss_engine.Text
# DSSCircuit = dss_engine.ActiveCircuit
# DSSSolution = dss_engine.ActiveCircuit.Solution
# ControlQueue = dss_engine.ActiveCircuit.CtrlQueue
# dss_engine.AllowForms = 0

# Variables
# data_array = [i for i in range(51)]
data = [0.1109592, -0.0774576, 0.0242556, -0.1598016, 0.035745, -0.0314556, 0.3658752, -0.156021, 0.1684332, 0.0421083, 0.0910391, 0.0563349, 0.009512, 0.0, 0.0, -0.05955, 0.152391, -0.237474, 0.2295658, 0.0906868, 0.1950606, 0.1309896, 0.049266, -0.100436, 0.0347772, -0.123864, 0.287859, 0.0, 0.040426, -0.171216, 0.4098545, -0.2968075, 0.368784, 0.0, 0.01189, 0.0, 0.0064287, -0.0069049, 0.3648969, 0.1766395, 0.0397992, -0.3603249, 0.0, -0.059525, 0.007131, 0.0, 0.0550536, -0.1891281, 238.07, 237.99, 237.64]
# transformer_voltage = round((data_array[48]+data_array[49]+data_array[50])/3,2) * math.sqrt(3)/1000

def calculteDss( data_array) ->list:
    # Set up DSS
    dss_engine = dss.DSS
    DSSText = dss_engine.Text
    DSSCircuit = dss_engine.ActiveCircuit
    DSSSolution = dss_engine.ActiveCircuit.Solution
    ControlQueue = dss_engine.ActiveCircuit.CtrlQueue
    dss_engine.AllowForms = 0
    OE_value = 0
    OE_max = 0
    OE_min = 0
    transformer_voltage = round((data_array[48] + data_array[49] + data_array[50]) / 3, 2) * math.sqrt(3) / 1000
    # Build the Circuit
    DSSText.Command = 'Clear'
    DSSText.Command = 'Set DefaultBaseFrequency=50'
    DSSText.Command = 'New Circuit.Capstone_LV_Network'
    DSSText.Command = 'Edit vsource.source bus1=sourceBus basekv=22 pu=1.0 phases=3'
    # Transformer
    DSSText.Command = f'New transformer.LVTR Buses=[sourcebus, NN1.1.2.3] Conns=[delta wye] KVs=[22, {transformer_voltage}] KVAs=[500 500] '
    #line
    DSSText.Command = 'New Line.BB1 Bus1=NN1.1.2.3 Bus2=NN2.1.2.3 Phases=3 R1=0.052 X1=0.05 R0=0.31 X0=0.155 Normamps=141'
    DSSText.Command = 'New Line.BB2 Bus1=NN2.1.2.3 Bus2=NN3.1.2.3 Phases=3 R1=0.045 X1=0.000001 R0=0.141 X0=0.03 Normamps=141'
    DSSText.Command = 'New Line.BB3 Bus1=NN3.1.2.3 Bus2=NN4.1.2.3 Phases=3 R1=0.119 X1=0.095 R0=0.2675 X0=0.161 Normamps=107'
    DSSText.Command = 'New Line.BB4 Bus1=NN4.1.2.3 Bus2=NN5.1.2.3 Phases=3 R1=0.092 X1=0.082 R0=0.344 X0=0.22 Normamps=107'
    DSSText.Command = 'New Line.BB5 Bus1=NN2.1.2.3 Bus2=NN6.1.2.3 Phases=3 R1=0.028 X1=0.000001 R0=0.154 X0=0.000001 Normamps=107'
    DSSText.Command = 'New Line.BB6 Bus1=NN6.1.2.3 Bus2=NN7.1.2.3 Phases=3 R1=0.055 X1=0.000001 R0=0.163 X0=0.024 Normamps=107'
    DSSText.Command = 'New Line.BB7 Bus1=NN6.1.2.3 Bus2=NN8.1.2.3 Phases=3 R1=0.043 X1=0.000001 R0=0.334 X0=0.000001 Normamps=107'
    DSSText.Command = 'New Line.BB8 Bus1=NN8.1.2.3 Bus2=NN9.1.2.3 Phases=3 R1=0.067 X1=0.000001 R0=0.229 X0=0.032 Normamps=107'
    DSSText.Command = 'New Line.SC1 Bus1=NN5.1.2.3 Bus2=CN1.1.2.3 Phases=3 R1=0.125 X1=0.019 R0=0.326 X0=0.028 Normamps=500'
    DSSText.Command = 'New Line.SC2 Bus1=NN8.1 Bus2=CN2.1 Phases=1 R1=0.052 X1=0.001 R0=0.052 X0=0.001 Normamps=100'
    DSSText.Command = 'New Line.SC3 Bus1=NN7.1.2.3 Bus2=CN3.1.2.3 Phases=3 R1=0.07 X1=0.000001 R0=0.187 X0=0.042 Normamps=100'
    DSSText.Command = 'New Line.SC4 Bus1=NN4.2 Bus2=CN4.2 Phases=1 R1=0.116 X1=0.000001 R0=0.116 X0=0.000001 Normamps=100'
    DSSText.Command = 'New Line.SC5 Bus1=NN9.2 Bus2=CN5.2 Phases=1 R1=0.169 X1=0.000001 R0=0.169 X0=0.000001 Normamps=100'
    DSSText.Command = 'New Line.SC6 Bus1=NN9.3 Bus2=CN6.3 Phases=1 R1=0.138 X1=0.000001 R0=0.138 X0=0.000001 Normamps=100'
    DSSText.Command = 'New Line.SC7 Bus1=NN7.1.2.3 Bus2=CN7.1.2.3 Phases=3 R1=0.055 X1=0.11 R0=0.286 X0=0.116 Normamps=100'
    DSSText.Command = 'New Line.SC8 Bus1=NN3.3 Bus2=CN8.3 Phases=1 R1=0.102 X1=0.000001 R0=0.102 X0=0.000001 Normamps=100'
    DSSText.Command = 'New Line.SC9 Bus1=NN9.1.2.3 Bus2=CN9.1.2.3 Phases=3 R1=0.102333 X1=0.000001 R0=0.336333 X0=0.027333 Normamps=100'
    DSSText.Command = 'New Line.SC10 Bus1=NN2.2 Bus2=CN10.2 Phases=1 R1=0.041 X1=0.033 R0=0.041 X0=0.033 Normamps=100'
    DSSText.Command = 'New Line.SC11 Bus1=NN5.2 Bus2=CN11.2 Phases=1 R1=0.153 X1=0.285 R0=0.153 X0=0.285 Normamps=100'
    DSSText.Command = 'New Line.SC12 Bus1=NN3.1.2.3 Bus2=CN12.1.2.3 Phases=3 R1=0.049 X1=0.000001 R0=0.073 X0=0.06 Normamps=100'
    DSSText.Command = 'New Line.SC13 Bus1=NN9.1 Bus2=CN13.1 Phases=1 R1=0.097 X1=0.001 R0=0.097 X0=0.001 Normamps=100'
    DSSText.Command = 'New Line.SC14 Bus1=NN4.1 Bus2=CN14.1 Phases=1 R1=0.134 X1=0.013 R0=0.134 X0=0.013 Normamps=100'
    DSSText.Command = 'New Line.SC15 Bus1=NN1.1.2.3 Bus2=CN15.1.2.3 Phases=3 R1=0.000001 X1=0.000001 R0=0.000001 X0=0.000001 Normamps=100'

    # # Loads
    DSSText.Command = f'new load.B1_a bus1=CN1.1 phases=1 kV=(0.4 3 sqrt /) kW={data_array[0]} kva={data_array[1]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B1_b bus1=CN1.2 phases=1 kV=(0.4 3 sqrt /) kW={data_array[2]} kva={data_array[3]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B1_c bus1=CN1.3 phases=1 kV=(0.4 3 sqrt /) kW={data_array[4]} kva={data_array[5]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B2_a bus1=CN2.1 phases=1 kV=(0.4 3 sqrt /) kW={data_array[20]} kva={data_array[21]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B3_a bus1=CN3.1 phases=1 kV=(0.4 3 sqrt /) kW={data_array[22]} kva={data_array[23]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B3_b bus1=CN3.2 phases=1 kV=(0.4 3 sqrt /) kW={data_array[24]} kva={data_array[25]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B3_c bus1=CN3.3 phases=1 kV=(0.4 3 sqrt /) kW={data_array[26]} kva={data_array[27]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B4_b bus1=CN4.2 phases=1 kV=(0.4 3 sqrt /) kW={data_array[28]} kva={data_array[29]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B5_b bus1=CN5.2 phases=1 kV=(0.4 3 sqrt /) kW={data_array[30]} kva={data_array[31]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B6_c bus1=CN6.3 phases=1 kV=(0.4 3 sqrt /) kW={data_array[32]} kva={data_array[33]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B7_a bus1=CN7.1 phases=1 kV=(0.4 3 sqrt /) kW={data_array[34]} kva={data_array[35]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B7_b bus1=CN7.2 phases=1 kV=(0.4 3 sqrt /) kW={data_array[36]} kva={data_array[37]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B7_c bus1=CN7.3 phases=1 kV=(0.4 3 sqrt /) kW={data_array[38]} kva={data_array[39]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B8_c bus1=CN8.3 phases=1 kV=(0.4 3 sqrt /) kW={data_array[40]} kva={data_array[41]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B9_a bus1=CN9.1 phases=1 kV=(0.4 3 sqrt /) kW={data_array[42]} kva={data_array[43]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B9_b bus1=CN9.2 phases=1 kV=(0.4 3 sqrt /) kW={data_array[44]} kva={data_array[45]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B9_c bus1=CN9.3 phases=1 kV=(0.4 3 sqrt /) kW={data_array[46]} kva={data_array[47]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B10_b bus1=CN10.2 phases=1 kV=(0.4 3 sqrt /) kW={data_array[6]} kva={data_array[7]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B11_b bus1=CN11.2 phases=1 kV=(0.4 3 sqrt /) kW={data_array[8]} kva={data_array[9]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B12_a bus1=CN12.1 phases=1 kV=(0.4 3 sqrt /) kW={data_array[10]} kva={data_array[11]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B12_b bus1=CN12.2 phases=1 kV=(0.4 3 sqrt /) kW={data_array[12]} kva={data_array[13]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B12_c bus1=CN12.3 phases=1 kV=(0.4 3 sqrt /) kW={data_array[14]} kva={data_array[15]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B13_a bus1=CN13.1 phases=1 kV=(0.4 3 sqrt /) kW={data_array[16]} kva={data_array[17]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    DSSText.Command = f'new load.B14_a bus1=CN14.1 phases=1 kV=(0.4 3 sqrt /) kW={data_array[18]} kva={data_array[19]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
    # Configure
    DSSText.Command = 'set controlmode=static'
    DSSText.Command = 'set mode=snapshot'
    DSSText.Command = 'Set VoltageBases=[22 0.4]'
    DSSText.Command = 'calcvoltagebases'

    # Solve the Circuit
    DSSSolution.Solve()

    bus_lst_3 = ["CN1", "CN3", "CN7", "CN9", "CN12"]
    bus_lst_1 = ["CN2", "CN4", "CN5", "CN6", "CN8", "CN10", "CN11", "CN13", "CN14"]
    line_names = ['bb1', 'bb2', 'bb3', 'bb4', 'bb5', 'bb6', 'bb7', 'bb8', 'sc1', 'sc2', 'sc3', 'sc4', 'sc5', 'sc6',
                  'sc7', 'sc8', 'sc9', 'sc10', 'sc11', 'sc12', 'sc13', 'sc14', 'sc15']
    line_thermal = [141] * 2 + [107] * 6 + [500] + [100] * 14
    check = 0
    tolerance = 0.01
    upper_bound = 0
    lower_bound = -14.01
    mid = (upper_bound - lower_bound) / 2

    OE_value = mid
    DSSSolution.Solve()
    for item in bus_lst_3:
        active_bus = item
        DSSCircuit.SetActiveBus(active_bus)
        if DSSCircuit.ActiveBus.puVmagAngle[0] > 1.1 or DSSCircuit.ActiveBus.puVmagAngle[2] > 1.1 or \
                DSSCircuit.ActiveBus.puVmagAngle[4] > 1.1:
            check = 1
            break
    for item in bus_lst_1:
        active_bus = item
        DSSCircuit.SetActiveBus(active_bus)
        if DSSCircuit.ActiveBus.puVmagAngle[0] > 1.1:
            check = 1
            break
    # 热限制
    for iLine in range(len(line_names)):
        DSSCircuit.SetActiveElement('Line.' + line_names[iLine])

        number_phases = int(DSSCircuit.ActiveElement.Properties('Phases').Val)

        if number_phases == 3:
            I11 = DSSCircuit.ActiveCktElement.CurrentsMagAng[0]
            I12 = DSSCircuit.ActiveCktElement.CurrentsMagAng[2]
            I13 = DSSCircuit.ActiveCktElement.CurrentsMagAng[4]
            I_rated = DSSCircuit.Lines.NormAmps
            I_max_lv_oe_temp = max(I11, I12, I13)
            print(I_max_lv_oe_temp, I_rated)
            if I_max_lv_oe_temp > I_rated:
                check = 1
                break
        elif number_phases == 1:
            I11 = DSSCircuit.ActiveCktElement.CurrentsMagAng[0]
            I_rated = DSSCircuit.Lines.NormAmps
            if I11 > I_rated:
                check = 1
                break

    if check == 0:
        upper_bound = mid
    else:
        lower_bound = mid
    mid = (upper_bound + lower_bound) / 2



    OE_min = round(upper_bound, 2)

    # -----------------------------------------------------------------
    check = 0
    upper_bound = 10.00
    lower_bound = 0
    mid = (upper_bound - lower_bound) / 2

    while upper_bound - lower_bound > tolerance:
        OE_value = mid
        DSSSolution.Solve()
        for item in bus_lst_3:
            active_bus = item
            DSSCircuit.SetActiveBus(active_bus)
            if DSSCircuit.ActiveBus.puVmagAngle[0] < 0.94 or \
                    DSSCircuit.ActiveBus.puVmagAngle[2] < 0.94 or \
                    DSSCircuit.ActiveBus.puVmagAngle[4] < 0.94:
                check = 1
                break
        for item in bus_lst_1:
            active_bus = item
            DSSCircuit.SetActiveBus(active_bus)
            if DSSCircuit.ActiveBus.puVmagAngle[0] < 0.94:
                check = 1
                break

        if check == 0:
            lower_bound = mid
        else:
            upper_bound = mid
        mid = (upper_bound + lower_bound) / 2

    OE_max = round(upper_bound, 2)


    end_time = time.time()



    total_time = end_time - start_time


    return [OE_max,-OE_min]












# Data read code goes here #
# OE_value = 0
# OE_max = 0
# OE_min = 0
#
# # Build the Circuit
# DSSText.Command = 'Clear'
# DSSText.Command = 'Set DefaultBaseFrequency=50'
# DSSText.Command = 'New Circuit.Capstone_LV_Network'
# DSSText.Command = 'Edit vsource.source bus1=sourceBus basekv=22 pu=1.0 phases=3'
#
# # Transformer
# DSSText.Command = f'New transformer.LVTR Buses=[sourcebus, NN1.1.2.3] Conns=[delta wye] KVs=[22, {transformer_voltage}] KVAs=[500 500] '
#
# # Lines
# DSSText.Command = 'New Line.BB1 Bus1=NN1.1.2.3 Bus2=NN2.1.2.3 Phases=3 R1=0.052 X1=0.05 R0=0.31 X0=0.155 Normamps=141'
# DSSText.Command = 'New Line.BB2 Bus1=NN2.1.2.3 Bus2=NN3.1.2.3 Phases=3 R1=0.045 X1=0.000001 R0=0.141 X0=0.03 Normamps=141'
# DSSText.Command = 'New Line.BB3 Bus1=NN3.1.2.3 Bus2=NN4.1.2.3 Phases=3 R1=0.119 X1=0.095 R0=0.2675 X0=0.161 Normamps=107'
# DSSText.Command = 'New Line.BB4 Bus1=NN4.1.2.3 Bus2=NN5.1.2.3 Phases=3 R1=0.092 X1=0.082 R0=0.344 X0=0.22 Normamps=107'
# DSSText.Command = 'New Line.BB5 Bus1=NN2.1.2.3 Bus2=NN6.1.2.3 Phases=3 R1=0.028 X1=0.000001 R0=0.154 X0=0.000001 Normamps=107'
# DSSText.Command = 'New Line.BB6 Bus1=NN6.1.2.3 Bus2=NN7.1.2.3 Phases=3 R1=0.055 X1=0.000001 R0=0.163 X0=0.024 Normamps=107'
# DSSText.Command = 'New Line.BB7 Bus1=NN6.1.2.3 Bus2=NN8.1.2.3 Phases=3 R1=0.043 X1=0.000001 R0=0.334 X0=0.000001 Normamps=107'
# DSSText.Command = 'New Line.BB8 Bus1=NN8.1.2.3 Bus2=NN9.1.2.3 Phases=3 R1=0.067 X1=0.000001 R0=0.229 X0=0.032 Normamps=107'
# # DSSText.Command = 'New Line.SC1 Bus1=NN5.1.2.3 Bus2=CN1.1.2.3 Phases=3 R1=0.125 X1=0.019 R0=0.326 X0=0.028 Normamps=500'
# DSSText.Command = 'New Line.SC2 Bus1=NN8.1 Bus2=CN2.1 Phases=1 R1=0.052 X1=0.001 R0=0.052 X0=0.001 Normamps=100'
# DSSText.Command = 'New Line.SC3 Bus1=NN7.1.2.3 Bus2=CN3.1.2.3 Phases=3 R1=0.07 X1=0.000001 R0=0.187 X0=0.042 Normamps=100'
# DSSText.Command = 'New Line.SC4 Bus1=NN4.2 Bus2=CN4.2 Phases=1 R1=0.116 X1=0.000001 R0=0.116 X0=0.000001 Normamps=100'
# DSSText.Command = 'New Line.SC5 Bus1=NN9.2 Bus2=CN5.2 Phases=1 R1=0.169 X1=0.000001 R0=0.169 X0=0.000001 Normamps=100'
# DSSText.Command = 'New Line.SC6 Bus1=NN9.3 Bus2=CN6.3 Phases=1 R1=0.138 X1=0.000001 R0=0.138 X0=0.000001 Normamps=100'
# DSSText.Command = 'New Line.SC7 Bus1=NN7.1.2.3 Bus2=CN7.1.2.3 Phases=3 R1=0.055 X1=0.11 R0=0.286 X0=0.116 Normamps=100'
# DSSText.Command = 'New Line.SC8 Bus1=NN3.3 Bus2=CN8.3 Phases=1 R1=0.102 X1=0.000001 R0=0.102 X0=0.000001 Normamps=100'
# DSSText.Command = 'New Line.SC9 Bus1=NN9.1.2.3 Bus2=CN9.1.2.3 Phases=3 R1=0.102333 X1=0.000001 R0=0.336333 X0=0.027333 Normamps=100'
# DSSText.Command = 'New Line.SC10 Bus1=NN2.2 Bus2=CN10.2 Phases=1 R1=0.041 X1=0.033 R0=0.041 X0=0.033 Normamps=100'
# DSSText.Command = 'New Line.SC11 Bus1=NN5.2 Bus2=CN11.2 Phases=1 R1=0.153 X1=0.285 R0=0.153 X0=0.285 Normamps=100'
# DSSText.Command = 'New Line.SC12 Bus1=NN3.1.2.3 Bus2=CN12.1.2.3 Phases=3 R1=0.049 X1=0.000001 R0=0.073 X0=0.06 Normamps=100'
# DSSText.Command = 'New Line.SC13 Bus1=NN9.1 Bus2=CN13.1 Phases=1 R1=0.097 X1=0.001 R0=0.097 X0=0.001 Normamps=100'
# DSSText.Command = 'New Line.SC14 Bus1=NN4.1 Bus2=CN14.1 Phases=1 R1=0.134 X1=0.013 R0=0.134 X0=0.013 Normamps=100'
# DSSText.Command = 'New Line.SC15 Bus1=NN1.1.2.3 Bus2=CN15.1.2.3 Phases=3 R1=0.000001 X1=0.000001 R0=0.000001 X0=0.000001 Normamps=100'
# #
# # # # Loads
# DSSText.Command = f'new load.B1_a bus1=CN1.1 phases=1 kV=(0.4 3 sqrt /) kW={data_array[0]} kva={data_array[1]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B1_b bus1=CN1.2 phases=1 kV=(0.4 3 sqrt /) kW={data_array[2]} kva={data_array[3]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B1_c bus1=CN1.3 phases=1 kV=(0.4 3 sqrt /) kW={data_array[4]} kva={data_array[5]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B2_a bus1=CN2.1 phases=1 kV=(0.4 3 sqrt /) kW={data_array[20]} kva={data_array[21]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B3_a bus1=CN3.1 phases=1 kV=(0.4 3 sqrt /) kW={data_array[22]} kva={data_array[23]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B3_b bus1=CN3.2 phases=1 kV=(0.4 3 sqrt /) kW={data_array[24]} kva={data_array[25]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B3_c bus1=CN3.3 phases=1 kV=(0.4 3 sqrt /) kW={data_array[26]} kva={data_array[27]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B4_b bus1=CN4.2 phases=1 kV=(0.4 3 sqrt /) kW={data_array[28]} kva={data_array[29]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B5_b bus1=CN5.2 phases=1 kV=(0.4 3 sqrt /) kW={data_array[30]} kva={data_array[31]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B6_c bus1=CN6.3 phases=1 kV=(0.4 3 sqrt /) kW={data_array[32]} kva={data_array[33]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B7_a bus1=CN7.1 phases=1 kV=(0.4 3 sqrt /) kW={data_array[34]} kva={data_array[35]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B7_b bus1=CN7.2 phases=1 kV=(0.4 3 sqrt /) kW={data_array[36]} kva={data_array[37]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B7_c bus1=CN7.3 phases=1 kV=(0.4 3 sqrt /) kW={data_array[38]} kva={data_array[39]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B8_c bus1=CN8.3 phases=1 kV=(0.4 3 sqrt /) kW={data_array[40]} kva={data_array[41]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B9_a bus1=CN9.1 phases=1 kV=(0.4 3 sqrt /) kW={data_array[42]} kva={data_array[43]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B9_b bus1=CN9.2 phases=1 kV=(0.4 3 sqrt /) kW={data_array[44]} kva={data_array[45]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B9_c bus1=CN9.3 phases=1 kV=(0.4 3 sqrt /) kW={data_array[46]} kva={data_array[47]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B10_b bus1=CN10.2 phases=1 kV=(0.4 3 sqrt /) kW={data_array[6]} kva={data_array[7]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B11_b bus1=CN11.2 phases=1 kV=(0.4 3 sqrt /) kW={data_array[8]} kva={data_array[9]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B12_a bus1=CN12.1 phases=1 kV=(0.4 3 sqrt /) kW={data_array[10]} kva={data_array[11]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B12_b bus1=CN12.2 phases=1 kV=(0.4 3 sqrt /) kW={data_array[12]} kva={data_array[13]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B12_c bus1=CN12.3 phases=1 kV=(0.4 3 sqrt /) kW={data_array[14]} kva={data_array[15]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B13_a bus1=CN13.1 phases=1 kV=(0.4 3 sqrt /) kW={data_array[16]} kva={data_array[17]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
# DSSText.Command = f'new load.B14_a bus1=CN14.1 phases=1 kV=(0.4 3 sqrt /) kW={data_array[18]} kva={data_array[19]} model=1 conn=wye Vminpu=0.85 Vmaxpu=1.20 status=fixed'
#
# # # Configure
# DSSText.Command = 'set controlmode=static'
# DSSText.Command = 'set mode=snapshot'
# DSSText.Command = 'Set VoltageBases=[22 0.4]'
# DSSText.Command = 'calcvoltagebases'
#
# # Solve the Circuit
# DSSSolution.Solve()
# if DSSSolution.Converged:
#     print("The Circuit was Successfully Solved :-)")
#     print("\n")

#-----------------------------------------------------------------------------------------------------------------------
# bus_lst_3 = ["CN1","CN3","CN7","CN9","CN12"]
# bus_lst_1 = ["CN2","CN4","CN5","CN6","CN8","CN10","CN11","CN13","CN14"]
# line_names = ['bb1', 'bb2', 'bb3', 'bb4', 'bb5', 'bb6', 'bb7', 'bb8', 'sc1', 'sc2', 'sc3', 'sc4', 'sc5', 'sc6', 'sc7', 'sc8', 'sc9', 'sc10', 'sc11', 'sc12', 'sc13', 'sc14', 'sc15']
# line_thermal = [141]*2 + [107]*6 + [500] + [100]*14
# check = 0
# tolerance = 0.01
# upper_bound = 0
# lower_bound = -14.01
# # mid = (upper_bound-lower_bound)/2
# while upper_bound - lower_bound > tolerance:
#     OE_value = mid
#     DSSSolution.Solve()
#     for item in bus_lst_3:
#         active_bus = item
#         DSSCircuit.SetActiveBus(active_bus)
#         if DSSCircuit.ActiveBus.puVmagAngle[0]>1.1 or DSSCircuit.ActiveBus.puVmagAngle[2]>1.1 or DSSCircuit.ActiveBus.puVmagAngle[4]>1.1:
#             check = 1
#             break
#     for item in bus_lst_1:
#         active_bus = item
#         DSSCircuit.SetActiveBus(active_bus)
#         if DSSCircuit.ActiveBus.puVmagAngle[0]>1.1:
#             check = 1
#             break
#     # 热限制
#     for iLine in range(len(line_names)):
#         DSSCircuit.SetActiveElement('Line.'+line_names[iLine])
#         print(DSSCircuit.ActiveElement.Name)
#         number_phases = int(DSSCircuit.ActiveElement.Properties('Phases').Val)
#         print(line_names[iLine])
#         print(number_phases)
#         if number_phases == 3:
#             I11 = DSSCircuit.ActiveCktElement.CurrentsMagAng[0]
#             I12 = DSSCircuit.ActiveCktElement.CurrentsMagAng[2]
#             I13 = DSSCircuit.ActiveCktElement.CurrentsMagAng[4]
#             I_rated = DSSCircuit.Lines.NormAmps
#             I_max_lv_oe_temp = max(I11, I12, I13)
#             print(I_max_lv_oe_temp,I_rated)
#             if I_max_lv_oe_temp > I_rated:
#                 check = 1
#                 break
#         elif number_phases == 1:
#             I11 = DSSCircuit.ActiveCktElement.CurrentsMagAng[0]
#             I_rated = DSSCircuit.Lines.NormAmps
#             if I11 > I_rated:
#                 check = 1
#                 break
#
#
#     if check == 0:
#         upper_bound = mid
#     else:
#         lower_bound = mid
#     mid = (upper_bound + lower_bound)/2
#
# print('Answer is:')
# OE_min = round(upper_bound,2)
# print(OE_min)
# #-----------------------------------------------------------------
# check = 0
# upper_bound = 10.00
# lower_bound = 0
# mid = (upper_bound-lower_bound)/2
# while upper_bound - lower_bound > tolerance:
#     OE_value = mid
#     DSSSolution.Solve()
#     for item in bus_lst_3:
#         active_bus = item
#         DSSCircuit.SetActiveBus(active_bus)
#         if DSSCircuit.ActiveBus.puVmagAngle[0]<0.94 or \
#                 DSSCircuit.ActiveBus.puVmagAngle[2]<0.94 or \
#                 DSSCircuit.ActiveBus.puVmagAngle[4]<0.94:
#             check = 1
#             break
#     for item in bus_lst_1:
#         active_bus = item
#         DSSCircuit.SetActiveBus(active_bus)
#         if DSSCircuit.ActiveBus.puVmagAngle[0]<0.94:
#             check = 1
#             break
#
#     if check == 0:
#         lower_bound = mid
#     else:
#         upper_bound = mid
#     mid = (upper_bound + lower_bound)/2
# print('Answer is:')
# OE_max = round(upper_bound,2)
# print(OE_max)
#
# end_time = time.time()
#
# print(f'Export Limit is {OE_max}, Import Limit is {OE_min}')
#
# total_time = end_time - start_time
# print("程序执行时间为：", total_time, "秒")
