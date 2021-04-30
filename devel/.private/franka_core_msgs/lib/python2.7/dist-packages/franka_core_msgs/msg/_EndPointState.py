# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from franka_core_msgs/EndPointState.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class EndPointState(genpy.Message):
  _md5sum = "157e46b2d97e94a67549f0fd8090f80c"
  _type = "franka_core_msgs/EndPointState"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """std_msgs/Header header

float64[16] O_T_EE # Measured end effector pose in base frame

# ----- Moved ee velocity to robot state, because it is being computed using J*dq. EE vel is not being provided natively
#float64[6] O_dP_EE_c # Last commanded end effector twist in base frame.
#float64[6] O_dP_EE_d # Desired end effector twist in base frame.
#float64[6] O_ddP_EE_c # Last commanded end effector acceleration in base frame.

geometry_msgs/WrenchStamped O_F_ext_hat_K    # Estimated external wrench (force, torque) acting on stiffness frame, expressed relative to the base frame
geometry_msgs/WrenchStamped K_F_ext_hat_K    # Estimated external wrench (force, torque) acting on stiffness frame, expressed relative to the stiffness frame (ee_frame by default)




================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/WrenchStamped
# A wrench with reference coordinate frame and timestamp
Header header
Wrench wrench

================================================================================
MSG: geometry_msgs/Wrench
# This represents force in free space, separated into
# its linear and angular parts.
Vector3  force
Vector3  torque

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z"""
  __slots__ = ['header','O_T_EE','O_F_ext_hat_K','K_F_ext_hat_K']
  _slot_types = ['std_msgs/Header','float64[16]','geometry_msgs/WrenchStamped','geometry_msgs/WrenchStamped']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,O_T_EE,O_F_ext_hat_K,K_F_ext_hat_K

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(EndPointState, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.O_T_EE is None:
        self.O_T_EE = [0.] * 16
      if self.O_F_ext_hat_K is None:
        self.O_F_ext_hat_K = geometry_msgs.msg.WrenchStamped()
      if self.K_F_ext_hat_K is None:
        self.K_F_ext_hat_K = geometry_msgs.msg.WrenchStamped()
    else:
      self.header = std_msgs.msg.Header()
      self.O_T_EE = [0.] * 16
      self.O_F_ext_hat_K = geometry_msgs.msg.WrenchStamped()
      self.K_F_ext_hat_K = geometry_msgs.msg.WrenchStamped()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      buff.write(_get_struct_16d().pack(*self.O_T_EE))
      _x = self
      buff.write(_get_struct_3I().pack(_x.O_F_ext_hat_K.header.seq, _x.O_F_ext_hat_K.header.stamp.secs, _x.O_F_ext_hat_K.header.stamp.nsecs))
      _x = self.O_F_ext_hat_K.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_6d3I().pack(_x.O_F_ext_hat_K.wrench.force.x, _x.O_F_ext_hat_K.wrench.force.y, _x.O_F_ext_hat_K.wrench.force.z, _x.O_F_ext_hat_K.wrench.torque.x, _x.O_F_ext_hat_K.wrench.torque.y, _x.O_F_ext_hat_K.wrench.torque.z, _x.K_F_ext_hat_K.header.seq, _x.K_F_ext_hat_K.header.stamp.secs, _x.K_F_ext_hat_K.header.stamp.nsecs))
      _x = self.K_F_ext_hat_K.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_6d().pack(_x.K_F_ext_hat_K.wrench.force.x, _x.K_F_ext_hat_K.wrench.force.y, _x.K_F_ext_hat_K.wrench.force.z, _x.K_F_ext_hat_K.wrench.torque.x, _x.K_F_ext_hat_K.wrench.torque.y, _x.K_F_ext_hat_K.wrench.torque.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.O_F_ext_hat_K is None:
        self.O_F_ext_hat_K = geometry_msgs.msg.WrenchStamped()
      if self.K_F_ext_hat_K is None:
        self.K_F_ext_hat_K = geometry_msgs.msg.WrenchStamped()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 128
      self.O_T_EE = _get_struct_16d().unpack(str[start:end])
      _x = self
      start = end
      end += 12
      (_x.O_F_ext_hat_K.header.seq, _x.O_F_ext_hat_K.header.stamp.secs, _x.O_F_ext_hat_K.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.O_F_ext_hat_K.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.O_F_ext_hat_K.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 60
      (_x.O_F_ext_hat_K.wrench.force.x, _x.O_F_ext_hat_K.wrench.force.y, _x.O_F_ext_hat_K.wrench.force.z, _x.O_F_ext_hat_K.wrench.torque.x, _x.O_F_ext_hat_K.wrench.torque.y, _x.O_F_ext_hat_K.wrench.torque.z, _x.K_F_ext_hat_K.header.seq, _x.K_F_ext_hat_K.header.stamp.secs, _x.K_F_ext_hat_K.header.stamp.nsecs,) = _get_struct_6d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.K_F_ext_hat_K.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.K_F_ext_hat_K.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 48
      (_x.K_F_ext_hat_K.wrench.force.x, _x.K_F_ext_hat_K.wrench.force.y, _x.K_F_ext_hat_K.wrench.force.z, _x.K_F_ext_hat_K.wrench.torque.x, _x.K_F_ext_hat_K.wrench.torque.y, _x.K_F_ext_hat_K.wrench.torque.z,) = _get_struct_6d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      buff.write(self.O_T_EE.tostring())
      _x = self
      buff.write(_get_struct_3I().pack(_x.O_F_ext_hat_K.header.seq, _x.O_F_ext_hat_K.header.stamp.secs, _x.O_F_ext_hat_K.header.stamp.nsecs))
      _x = self.O_F_ext_hat_K.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_6d3I().pack(_x.O_F_ext_hat_K.wrench.force.x, _x.O_F_ext_hat_K.wrench.force.y, _x.O_F_ext_hat_K.wrench.force.z, _x.O_F_ext_hat_K.wrench.torque.x, _x.O_F_ext_hat_K.wrench.torque.y, _x.O_F_ext_hat_K.wrench.torque.z, _x.K_F_ext_hat_K.header.seq, _x.K_F_ext_hat_K.header.stamp.secs, _x.K_F_ext_hat_K.header.stamp.nsecs))
      _x = self.K_F_ext_hat_K.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_6d().pack(_x.K_F_ext_hat_K.wrench.force.x, _x.K_F_ext_hat_K.wrench.force.y, _x.K_F_ext_hat_K.wrench.force.z, _x.K_F_ext_hat_K.wrench.torque.x, _x.K_F_ext_hat_K.wrench.torque.y, _x.K_F_ext_hat_K.wrench.torque.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.O_F_ext_hat_K is None:
        self.O_F_ext_hat_K = geometry_msgs.msg.WrenchStamped()
      if self.K_F_ext_hat_K is None:
        self.K_F_ext_hat_K = geometry_msgs.msg.WrenchStamped()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 128
      self.O_T_EE = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=16)
      _x = self
      start = end
      end += 12
      (_x.O_F_ext_hat_K.header.seq, _x.O_F_ext_hat_K.header.stamp.secs, _x.O_F_ext_hat_K.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.O_F_ext_hat_K.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.O_F_ext_hat_K.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 60
      (_x.O_F_ext_hat_K.wrench.force.x, _x.O_F_ext_hat_K.wrench.force.y, _x.O_F_ext_hat_K.wrench.force.z, _x.O_F_ext_hat_K.wrench.torque.x, _x.O_F_ext_hat_K.wrench.torque.y, _x.O_F_ext_hat_K.wrench.torque.z, _x.K_F_ext_hat_K.header.seq, _x.K_F_ext_hat_K.header.stamp.secs, _x.K_F_ext_hat_K.header.stamp.nsecs,) = _get_struct_6d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.K_F_ext_hat_K.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.K_F_ext_hat_K.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 48
      (_x.K_F_ext_hat_K.wrench.force.x, _x.K_F_ext_hat_K.wrench.force.y, _x.K_F_ext_hat_K.wrench.force.z, _x.K_F_ext_hat_K.wrench.torque.x, _x.K_F_ext_hat_K.wrench.torque.y, _x.K_F_ext_hat_K.wrench.torque.z,) = _get_struct_6d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_16d = None
def _get_struct_16d():
    global _struct_16d
    if _struct_16d is None:
        _struct_16d = struct.Struct("<16d")
    return _struct_16d
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_6d = None
def _get_struct_6d():
    global _struct_6d
    if _struct_6d is None:
        _struct_6d = struct.Struct("<6d")
    return _struct_6d
_struct_6d3I = None
def _get_struct_6d3I():
    global _struct_6d3I
    if _struct_6d3I is None:
        _struct_6d3I = struct.Struct("<6d3I")
    return _struct_6d3I
