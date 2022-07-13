from utils import utils
import torch
import matplotlib.pyplot as plt

def plot_clusters_3Dpoints(points, cluster_ids, num_clusters, colab=False, out_path=None, filename=None):
    colors = torch.zeros((points.shape[0], 3))
    
    for id in range(num_clusters):
        color = torch.rand((3,))
        colors[cluster_ids == id] = color
    
    if colab == True:
        points = points.cpu().numpy()
        colors = colors.cpu().numpy()
        ax = plt.axes(projection='3d')
        ax.view_init(90, -90)
        ax.axis("off")
        ax.scatter(points[:,0], points[:,1], points[:,2], s=1, c=colors)

        if out_path is not None:
            filename = "surface_clusters_3D.png" if filename is None else filename
            plt.savefig(f"{out_path}/{filename}", dpi=300)

        plt.show()
    else:
        import open3d as o3d

        pcd = o3d.t.geometry.PointCloud(utils.torch2open3d(points))
        pcd.point["colors"] = utils.torch2open3d(colors)
        o3d.visualization.draw_geometries([pcd.to_legacy()])

def plot_clusters_2Dpoints(points, cluster_ids, num_clusters, out_path=None, filename=None):
    colors = torch.zeros((points.shape[0], 3))
    
    for id in range(num_clusters):
        color = torch.rand((3,))
        colors[cluster_ids == id] = color
    
    points = points.cpu().numpy()
    colors = colors.cpu().numpy()
    plt.scatter(points[:,0], points[:,1], s=1, c=colors)
    if out_path is not None:
        filename = "surface_clusters_2D.png" if filename is None else filename
        plt.savefig(f"{out_path}/{filename}", dpi=300)
    plt.show()