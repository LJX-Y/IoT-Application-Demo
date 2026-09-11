"""
数据处理器 - 简单的统计功能（后续可扩展）
"""


def calc_average(records, field="temperature"):
    """计算平均值"""
    values = [r[field] for r in records if field in r]
    return round(sum(values) / len(values), 1) if values else None


def calc_max_min(records, field="temperature"):
    """计算最大最小值"""
    values = [r[field] for r in records if field in r]
    if not values:
        return None, None
    return max(values), min(values)


def check_alert(record, threshold=30.0, field="temperature"):
    """温度超过阈值返回告警信息"""
    if field in record and record[field] > threshold:
        return f"设备 {record['device_id']} 温度异常: {record[field]}°C 超过阈值 {threshold}°C"
    return None
