def huber_loss(y_true, y_pred, delta=1.0):
	"""
	Compute the Huber Loss between true and predicted values.

	Args:
		y_true (float | list[float]): Ground truth values
		y_pred (float | list[float]): Predicted values
		delta (float): Transition threshold between MSE and MAE behavior

	Returns:
		float: Average Huber loss
	"""
	# Your code here
	if not isinstance(y_true,list):
		y_true,y_pred = [y_true],[y_pred]
	
	total = 0.0
	for yt, yp in zip(y_true,y_pred):
		error = abs(yp-yt)
		if error<=delta:
			total += error**2/2
		else:
			total += delta * (error-delta/2)

	return total/len(y_true)