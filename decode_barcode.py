from pyzbar.pyzbar import decode
import cv2
import numpy as np

# Read the image
image = cv2.imread("image3_barcode.jpg")

# Decode the barcode
barcodes = decode(image)
for barcode in barcodes:
    data = barcode.data.decode("utf-8")
    print(f"Barcode Data: {data}")

    # Extract polygon points
    points = barcode.polygon
    points = np.array([(point.x, point.y) for point in points], dtype=np.int32)

    # Expand the bounding box size
    scale_factor = 1.2  # Increase rectangle size by 20%
    centroid = np.mean(points, axis=0)  # Compute the center of the polygon
    expanded_points = np.array([centroid + scale_factor * (point - centroid) for point in points], dtype=np.int32)

    # Draw an expanded rectangle around the barcode
    cv2.polylines(image, [expanded_points], True, (0, 255, 0), 3)  # Thicker green rectangle

    # Annotate the decoded data beside the bounding box
    x, y = expanded_points[0]  # Use the first point of the bounding box
    cv2.putText(image, data, (int(x), int(y) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)  # Bigger text

# Display the image with the barcode highlighted and annotated
cv2.imshow("Barcode with Annotation", image)

# Wait for a key press
key = cv2.waitKey(0)

# Save the annotated image when a key is pressed
output_file = "decoded_barcode_expanded.png"
cv2.imwrite(output_file, image)
print(f"Annotated image saved as {output_file}")

cv2.destroyAllWindows()