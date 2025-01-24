import open3d as op
import copy as copy
import numpy as np

def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation)
    op.visualization.draw_geometries([source_temp, target_temp])
def The_FUN(file1,file2,threshold,trans_init,DRAW=0):

    source=op.io.read_point_cloud(file1)
    target= op.io.read_point_cloud(file2)

    processed_source, outlier_index = source.remove_radius_outlier(
                                                nb_points=16,
                                                radius=0.5)
        
    processed_target, outlier_index = target.remove_radius_outlier(
                                                nb_points=16,
        
                                                radius=0.5)
    reg_p2p = op.pipelines.registration.registration_icp(
    processed_source, processed_target, threshold, trans_init,
    op.pipelines.registration.TransformationEstimationPointToPoint(),
    op.pipelines.registration.ICPConvergenceCriteria(max_iteration=500))





    if DRAW==1:
        draw_registration_result(source, target, reg_p2p.transformation)

            
    #draw_registration_result(source, target, reg_p2p.transformation)
    op.geometry.PointCloud.transform(source,reg_p2p.transformation)
    if DRAW==1:
        draw_registration_result(source, target, reg_p2p.transformation)
    op.io.write_point_cloud("YOUR PATH\\TRANS_10.ply",source , write_ascii=False, compressed=False)

        
    
    return "file has been saved at location \n   YOUR PATH\\TRANS_10.ply"


    

    #saving





#threshold = 1
#DRAW=0
"""

trans_init = np.asarray([[0.983749,	0.179548,	0.000639952,	-109.266],
[-0.179369,	0.982916,	-0.0412659,	27.014],
[-0.00803822,	0.0404805,	0.999148,	-26.7991],
[0,	0,	0,	1]])
"""
#file1="D:\\cmti_works\\3d_rendering\\vidya_works\\m_codes\\PCL3 - Cloud.ply"
#file2="D:\\cmti_works\\3d_rendering\\vidya_works\\m_codes\\PCL1 - Cloud.ply"

#def caller(file1,file2,threshold,arr,DRAW):
#
#    #print(st)
#    arr=np.asarray(arr)
#    
#    return The_FUN(file1,file2 ,threshold,arr,DRAW)
#
array_2d = [[0 for _ in range(4)] for _ in range(4)]

def caller(stdstr1, stdstr2, threshold, check,utf8_text):
    data2=utf8_text.split()
    f_d=list()
    for i in data2:
        f_d.append(float(i))
    

    

    # Iterate over the input list and fill the 2D array
    for i in range(len(f_d)):
        row = i // 4  # Calculate the row index
        col = i % 4   # Calculate the column index
        array_2d[row][col] = f_d[i]
    trans_init=np.asarray(array_2d)



    
    
    
    return The_FUN(stdstr1,stdstr2 ,threshold,trans_init,check)
