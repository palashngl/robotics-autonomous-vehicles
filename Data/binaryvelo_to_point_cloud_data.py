
#import lib
import open3d as o3d # Open3D is an open-source library that supports rapid. development of software for 3D data processing, including scene reconstruction, visualization and 3D machine learning
import numpy as np
import struct
import glob
size_float = 4

file_to_open = sorted(glob.glob("/*.bin"))# location of the Source File  

for fi in file_to_open:
	list_pcd = []
	with open (fi, "rb") as f:
	    byte = f.read(size_float*4)
	    while byte:
	        x,y,z,intensity = struct.unpack("ffff", byte)
	        list_pcd.append([x, y, z])
	        byte = f.read(size_float*4)
	np_pcd = np.asarray(list_pcd)
	pcd = o3d.geometry.PointCloud()
	v3d = o3d.utility.Vector3dVector
	pcd.points = v3d(np_pcd)
	o3d.io.write_point_cloud(fi[:-3]+"pcd", pcd)
