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
    op.io.write_point_cloud("D:\\cmti_works\\3d_rendering\\vidya_works\\m_codes\\TRANS_10.ply",source , write_ascii=False, compressed=False)
    
        
    
    return "file has been saved at location \nD:\\cmti_works\\3d_rendering\\vidya_works\\m_codes\\TRANS_10.ply"


    

    #saving





threshold = 1
DRAW=1
trans_init = np.asarray([[0.983749,	0.179548,	0.000639952,	-109.266],
[-0.179369,	0.982916,	-0.0412659,	27.014],
[-0.00803822,	0.0404805,	0.999148,	-26.7991],
[0,	0,	0,	1]])
file1="D:\\cmti_works\\3d_rendering\\vidya_works\\m_codes\\PCL3 - Cloud.ply"
file2="D:\\cmti_works\\3d_rendering\\vidya_works\\m_codes\\PCL1 - Cloud.ply"

    
The_FUN(file1,file2 ,threshold,trans_init,DRAW)