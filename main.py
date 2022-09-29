import telemetryPlots

inputYear = int(input("Year: "))
inputRace = input("Race: ")
inputSession = input("Session: ")
inputDriver_1 = input("Driver1: ")
inputDriver_2 = input("Driver2: ")

option = input("T - Qualifying Fastest Telemetry Comparison \nM - Qualifying Fastets Minisector Comparison\n :")

if option == 'T':
    telemetryPlots.telemetryComparison(inputYear,inputSession,inputRace,inputDriver_1,inputDriver_2)
    print("COMPLETE SAVED COMPARISON IN FOLDER")

