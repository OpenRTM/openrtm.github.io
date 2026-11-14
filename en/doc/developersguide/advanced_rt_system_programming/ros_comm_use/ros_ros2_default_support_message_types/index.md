---
layout: page
title: "developer's guide"
---
<!-- Title: Serializer Names and ROS/ROS2 Message Types -->
#contents

When using the ROS or ROS2 communication features, OpenRTM-aist provides serializers corresponding to the following ROS/ROS2 message types.
If you need to use a message type other than those listed below, implement a custom serializer that converts data to the required message type.

<table class="table-alt">
  <tr>
    <th>Serializer Name</th>
    <th>RTM Data Type</th>
    <th>ROS/ROS2 Message Type</th>
  </tr>
  <tr>
    <td>ros:std_msgs/Float32,<br> ros2:std_msgs/Float32</td>
    <td>TimedState,TimedShort,<br> TimedLong,TimedUShort,<br> TimedULong,TimedFloat,<br> TimedDouble</td>
    <td>std_msgs/Float32</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Float64,<br> ros2:std_msgs/Float64</td>
    <td>TimedState,TimedShort,<br> TimedLong,TimedUShort,<br> TimedULong,TimedFloat,<br> TimedDouble</td>
    <td>std_msgs/Float64</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Int8,<br> ros2:std_msgs/Int8</td>
    <td>TimedState,TimedShort,<br> TimedLong,TimedUShort,<br> TimedULong,TimedFloat,<br> TimedDouble</td>
    <td>std_msgs/Int8</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Int16,<br> ros2:std_msgs/Int16</td>
    <td>TimedState,TimedShort,<br> TimedLong,TimedUShort,<br> TimedULong,TimedFloat,<br> TimedDouble</td>
    <td>std_msgs/Int16</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Int32,<br> ros2:std_msgs/Int32</td>
    <td>TimedState,TimedShort,<br> TimedLong,TimedUShort,<br> TimedULong,TimedFloat,<br> TimedDouble</td>
    <td>std_msgs/UInt8</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Int64,<br> ros2:std_msgs/Int64</td>
    <td>TimedState,TimedShort,<br> TimedLong,TimedUShort,<br> TimedULong,TimedFloat,<br> TimedDouble</td>
    <td>std_msgs/UInt16</td>
  </tr>
  <tr>
    <td>ros:std_msgs/UInt32,<br> ros2:std_msgs/UInt32</td>
    <td>TimedState,TimedShort,<br> TimedLong,TimedUShort,<br> TimedULong,TimedFloat,<br> TimedDouble</td>
    <td>std_msgs/UInt32</td>
  </tr>
  <tr>
    <td>ros:std_msgs/UInt64,<br> ros2:std_msgs/UInt64</td>
    <td>TimedState,TimedShort,<br> TimedLong,TimedUShort,<br> TimedULong,TimedFloat,<br> TimedDouble</td>
    <td>std_msgs/UInt64</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Float32MultiArray,<br> ros2:std_msgs/Float32MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq,TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/Float32MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Float32MultiArray,<br> ros2:std_msgs/Float32MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq,TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/Float32MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Float64MultiArray,<br> ros2:std_msgs/Float64MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq, TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/Float64MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Int8MultiArray,<br> ros2:std_msgs/Int8MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq,TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/Int8MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Int16MultiArray,<br> ros2:std_msgs/Int16MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq,TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/Int16MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Int32MultiArray,<br> ros2:std_msgs/Int32MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq,TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/Int32MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Int64MultiArray,<br> ros2:std_msgs/Int64MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq,TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/Int64MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/UInt8MultiArray,<br> ros2:std_msgs/UInt8MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq,TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/UInt8MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/UInt16MultiArray,<br> ros2:std_msgs/UInt16MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq,TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/UInt16MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/UInt32MultiArray,<br> ros2:std_msgs/UInt32MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq,TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/UInt32MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/UInt64MultiArray,<br> ros2:std_msgs/UInt64MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq,TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/UInt64MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/String,<br> ros2:std_msgs/String</td>
    <td>TimedString</td>
    <td>std_msgs/String</td>
  </tr>
  <tr>
    <td>ros:geometry_msgs/PointStamped,<br> ros2:geometry_msgs/PointStamped</td>
    <td>TimedPoint3D</td>
    <td>geometry_msgs/PointStamped</td>
  </tr>
  <tr>
    <td>ros:geometry_msgs/QuaternionStamped,<br> ros2:geometry_msgs/QuaternionStamped</td>
    <td>TimedQuaternion</td>
    <td>geometry_msgs/QuaternionStamped</td>
  </tr>
  <tr>
    <td>ros:geometry_msgs/Vector3Stamped,<br> ros2:geometry_msgs/Vector3Stamped</td>
    <td>TimedVector3D</td>
    <td>geometry_msgs/Vector3Stamped</td>
  </tr>
  <tr>
    <td>ros:sensor_msgs/Image,<br> ros2:sensor_msgs/Image</td>
    <td>CameraImage</td>
    <td>sensor_msgs/Image</td>
  </tr>
</table>

