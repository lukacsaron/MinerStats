'use strict'
import config
import requests
import json
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
#import pdb;pdb.set_trace()




#Define Google Sheets scope, creds and sheet
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('config.json', scope)
client = gspread.authorize(creds)
spreadsheetname = config.google_config['sheetname']
sheet = client.open(spreadsheetname)
sheet_instance = sheet.get_worksheet(0)
history_sheet = sheet.get_worksheet(1)


try:
    #Define Current Time
    current_time = datetime.datetime.now()
    
    #Preload the spreadsheet with Labels
    sheet_instance.update_acell('A1', 'Ethereum Calculator')
    sheet_instance.update_acell('A2', 'Last Updated')
    sheet_instance.update_acell('B2', str(current_time))
    sheet_instance.update_acell('A4', 'Realtime ETH Network Stats')
    sheet_instance.update_acell('A5', 'Network Rate')
    sheet_instance.update_acell('A6', 'Block Time')
    sheet_instance.update_acell('A7', 'Block Reward')
    sheet_instance.update_acell('A8', 'Blocks 1D')

    sheet_instance.update_acell('A13', 'Currencies')
    sheet_instance.update_acell('A14', 'ETH/USD')
    sheet_instance.update_acell('A15', 'USD/HUF')
    sheet_instance.update_acell('B8', '=SUM(86400/B6)')
    sheet_instance.update_acell('B15', '=GoogleFinance("CURRENCY:USDHUF")')

    sheet_instance.update_acell('D4', 'Rig Stats for')
    sheet_instance.update_acell('E4', 'rig_name')
    sheet_instance.update_acell('D5', 'Rig Hash Rate')
    sheet_instance.update_acell('D6', 'Rig Power Watts')
    sheet_instance.update_acell('D7', 'Power Cost KW/H (HUF)')
    sheet_instance.update_acell('D8', 'Power Cost KW/H (USD)')
    sheet_instance.update_acell('D9', 'Mining Prob')
    sheet_instance.update_acell('E9', '=SUM(E5/B5)')
    sheet_instance.update_acell('D10', 'Est Blocks per Month')
    sheet_instance.update_acell('E10', '=SUM(E9*B8)')
    sheet_instance.update_acell('G1', 'PSU Efficiency')
    sheet_instance.update_acell('G2', '0.80')
    sheet_instance.update_acell('H1', 'Pool Fee')
    #pool_fee = input("How much is your pool fee? (enter decimal numbers, like 0.03)")
    sheet_instance.update_acell('H2', '0')
    sheet_instance.update_acell('G4', 'Rig Economics (USD)')
    sheet_instance.update_acell('H5', '24H')
    sheet_instance.update_acell('I5', '30D')
    sheet_instance.update_acell('J5', '1Y')
    sheet_instance.update_acell('G6', 'Revenue')
    sheet_instance.update_acell('G7', 'Pool Fee')
    sheet_instance.update_acell('G8', 'Cost')
    sheet_instance.update_acell('G9', 'Profit')
    sheet_instance.update_acell('H6' , '=SUM((B7)*(E9*B8))*B14')
    sheet_instance.update_acell('H7' , '=SUM(H6*H2)')
    sheet_instance.update_acell('H8' , '=SUM((((E6+(E6*(1-G2)))/1000))*E8)*24')
    sheet_instance.update_acell('H9' , '=SUM(H6-H7-H8)')
    sheet_instance.update_acell('I6' , '=SUM(H6*30)')
    sheet_instance.update_acell('I7' , '=SUM(H7*30)')
    sheet_instance.update_acell('I8' , '=SUM(H8*30)')
    sheet_instance.update_acell('I9' , '=SUM(H9*30)')
    sheet_instance.update_acell('J6' , '=SUM(H6*365)')
    sheet_instance.update_acell('J7' , '=SUM(H7*365)')
    sheet_instance.update_acell('J8' , '=SUM(H8*365)')
    sheet_instance.update_acell('J9' , '=SUM(H9*365)')
    sheet_instance.update_acell('G11', 'Rig Economics (HUF)')
    sheet_instance.update_acell('H12', '24H')
    sheet_instance.update_acell('I12', '30D')
    sheet_instance.update_acell('J12', '1Y')
    sheet_instance.update_acell('G13', 'Revenue')
    sheet_instance.update_acell('G14', 'Pool Fee')
    sheet_instance.update_acell('G15', 'Cost')  
    sheet_instance.update_acell('G16', 'Profit')
    sheet_instance.update_acell('H13', '=H6*$B$15')
    sheet_instance.update_acell('H14', '=H7*$B$15')
    sheet_instance.update_acell('H15', '=H8*$B$15')
    sheet_instance.update_acell('H16', '=H9*$B$15')
    sheet_instance.update_acell('I13', '=I6*$B$15')
    sheet_instance.update_acell('I14', '=I7*$B$15')
    sheet_instance.update_acell('I15', '=I8*$B$15')
    sheet_instance.update_acell('I16', '=I9*$B$15')
    sheet_instance.update_acell('J13', '=J6*$B$15')
    sheet_instance.update_acell('J14', '=J7*$B$15')
    sheet_instance.update_acell('J15', '=J8*$B$15')
    sheet_instance.update_acell('J16', '=J9*$B$15')


    #Populate Initial History Table
    history_sheet.update_acell('A1', 'current_time')
    history_sheet.update_acell('B1', 'current_eth_usd')
    history_sheet.update_acell('C1', 'current_eth_rate')
    history_sheet.update_acell('D1', 'current_eth_blocktime')
    history_sheet.update_acell('E1', 'current_eth_blockreward')
    history_sheet.update_acell('F1', 'eth_network_block1d')
    history_sheet.update_acell('G1', 'rig_name')
    history_sheet.update_acell('H1', 'reported_rig_hashrate')
    history_sheet.update_acell('I1', 'power_draw')
    history_sheet.update_acell('J1', 'power_cost')
    history_sheet.update_acell('K1', 'rig_prob')
    history_sheet.update_acell('L1', 'rig_blocks_30d')
    history_sheet.update_acell('M1', 'psu_eff')
    history_sheet.update_acell('N1', 'pool_fee')
    history_sheet.update_acell('O1', '24h_rev')
    history_sheet.update_acell('P1', '24h_fee')
    history_sheet.update_acell('Q1', '24h_cost')
    history_sheet.update_acell('R1', '24h_profit')
    history_sheet.update_acell('S1', '30d_rev')
    history_sheet.update_acell('T1', '30d_fee')
    history_sheet.update_acell('U1', '30d_cost')
    history_sheet.update_acell('V1', '30d_profit')
    history_sheet.update_acell('W1', '1y_rev')
    history_sheet.update_acell('X1', '1y_fee')
    history_sheet.update_acell('Y1', '1y_cost')
    history_sheet.update_acell('Z1', '1y_profit')

    #Print Success Message
    print("The initial spreadsheet has been created successfully")

except:
    #Print Console Message - Error
    print("An exception occurred")