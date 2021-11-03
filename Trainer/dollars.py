# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"\$(\d+\.?\d*)\b"

test_str = ("Date, Close/Last, Volume, Open, High, Low\n"
	"06/02/2020, $323.34, 21910700, $320.745, $323.44, $318.93\n"
	"06/01/2020, $321.85, 20254650, $317.75, $322.35, $317.21\n"
	"05/29/2020, $317.94, 38399530, $319.25, $321.15, $316.47\n"
	"05/28/2020, $318.25, 33449100, $316.77, $323.44, $315.63\n"
	"05/27/2020, $318.11, 28236270, $316.14, $318.71, $313.09\n"
	"05/26/2020, $316.73, 31380450, $323.5, $324.24, $316.5\n"
	"05/22/2020, $318.89, 20450750, $315.77, $319.23, $315.35\n"
	"05/21/2020, $316.85, 25672210, $318.66, $320.89, $315.87\n"
	"05/20/2020, $319.23, 27876220, $316.68, $319.52, $316.2\n"
	"05/19/2020, $313.14, 25432390, $315.03, $318.52, $313.01\n"
	"05/18/2020, $314.96, 33843130, $313.17, $316.5, $310.3241\n"
	"05/15/2020, $307.71, 41587090, $300.35, $307.9, $300.21\n"
	"05/14/2020, $309.54, 39732270, $304.51, $309.79, $301.53\n"
	"05/13/2020, $307.65, 50155640, $312.15, $315.95, $303.21\n"
	"05/12/2020, $311.41, 40575260, $317.83, $319.688, $310.91\n"
	"05/11/2020, $315.01, 36486560, $308.1, $317.05, $307.24\n"
	"05/08/2020, $310.13, 33511990, $305.64, $310.35, $304.29\n"
	"05/07/2020, $303.74, 28803760, $303.22, $305.17, $301.97\n"
	"05/06/2020, $300.63, 35583440, $300.46, $303.24, $298.87\n"
	"05/05/2020, $297.56, 36937800, $295.06, $301, $294.46\n"
	"05/04/2020, $293.16, 33391990, $289.17, $293.69, $286.3172\n"
	"05/01/2020, $289.07, 60154180, $286.25, $299, $285.85\n"
	"04/30/2020, $293.8, 45765970, $289.96, $294.53, $288.35\n"
	"04/29/2020, $287.73, 34320200, $284.73, $289.67, $283.89\n"
	"04/28/2020, $278.58, 28001190, $285.08, $285.83, $278.2\n"
	"04/27/2020, $283.17, 29271890, $281.8, $284.54, $279.95\n"
	"04/24/2020, $282.97, 31627180, $277.2, $283.01, $277\n"
	"04/23/2020, $275.03, 31203580, $275.87, $281.75, $274.87\n"
	"04/22/2020, $276.1, 29264340, $273.61, $277.9, $272.2\n"
	"04/21/2020, $268.37, 45247890, $276.28, $277.25, $265.43\n"
	"04/20/2020, $276.93, 32503750, $277.95, $281.68, $276.85\n"
	"04/17/2020, $282.8, 53812480, $284.69, $286.945, $276.86\n"
	"04/16/2020, $286.69, 39281290, $287.38, $288.1975, $282.3502")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))