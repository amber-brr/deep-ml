def balance_undersample(data: list) -> list:
    """
    Undersample the majority classes so all classes have the same number of
    samples equal to the minority class count.

    data: list of (sample, label) tuples
    Returns: list of (sample, label) tuples, order-preserving
    """
    freq = {}
    ans = []
    if not data:
        return []
    for i,(sample, label) in enumerate(data):
        freq.setdefault(label, []).append(i)
    min_len = min([len(i_s) for i_s in freq.values()])
    keep = {i for i_s in freq.values() for i in i_s[:min_len]}
    return [item for i,item in enumerate(data) if i in keep]
