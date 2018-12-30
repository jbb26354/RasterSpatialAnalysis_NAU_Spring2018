# ---------------------------------------------------------------------------
# GSP537.py
# Created on: 2018-04-23 21:02:36.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: GSP 537 Spring 2018 Lab 7
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Load required toolboxes
arcpy.ImportToolbox("Model Functions")

# Local variables:
ASTER_gdb = "X:\\Hostgator\\homework\\Courses\\GSP537\\labs\\7\\data\\ASTER.gdb"
Name = "AST17042B1"
AST17042B1 = "X:\\Hostgator\\homework\\Courses\\GSP537\\labs\\7\\data\\ASTER.gdb\\AST17042B1"
v_Name__UTM = "X:\\Hostgator\\homework\\Courses\\GSP537\\labs\\7\\data\\ASTER.gdb\\%Name%_UTM"
MBR = "X:\\Hostgator\\homework\\Courses\\GSP537\\labs\\7\\data\\Schultz.gdb\\UTM12N\\MBR"
v_Name_ = "X:\\Hostgator\\homework\\Courses\\GSP537\\labs\\7\\data\\Schultz.gdb\\%Name%"

# Process: Iterate Rasters
arcpy.IterateRasters_mb(ASTER_gdb, "AST*", "", "NOT_RECURSIVE")

# Process: Project Raster
arcpy.ProjectRaster_management(AST17042B1, v_Name__UTM, "PROJCS['NAD_1983_UTM_Zone_12N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-111.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", "NEAREST", "15 15", "WGS_1984_(ITRF00)_To_NAD_1983", "", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")

# Process: Clip
arcpy.Clip_management(v_Name__UTM, "435026.1841 3898226.1314 455134.5576 3919045.5741", v_Name_, MBR, "", "NONE", "NO_MAINTAIN_EXTENT")
