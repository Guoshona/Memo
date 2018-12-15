
//获取绘制的多边形
IGeometry drawGeo = _mapControl.TrackPolygon();
//判断绘制多边形是否为null，并不为空图形
if (drawGeo != null && !drawGeo.IsEmpty)
{
     //图形转为点集
     IPointCollection pPointColl = drawGeo as IPointCollection;
     //遍历点集
     for (int i = 0; i < pPointColl.PointCount; i++)
     {
          //获取点
          IPoint pPoint = pPointColl.get_Point(i);
          //输出点坐标
          Console.WriteLine("x:" + pPoint.X.ToString("f2") + ", y:" + pPoint.Y.ToString("f2"));
      }
}
