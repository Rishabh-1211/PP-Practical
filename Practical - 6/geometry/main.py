from geometry import squareArea, circleArea

def pointyShapeVolume(x, y, squareBase):
    """
    Calculate the volume of a square pyramid or a right circular cone.

    Parameters:
    - x: edge length if squareBase is True, radius if False
    - y: height of the shape
    - squareBase: True for square pyramid, False for cone

    Returns:
    - Volume of the shape
    """
    if squareBase:
        base_area = squareArea(x)
    else:
        base_area = circleArea(x)

    volume = (1 / 3) * base_area * y
    return volume

def main():
    # Square pyramid
    edge = float(input("Enter the edge length of the square base: "))
    height = float(input("Enter the height of the square pyramid: "))
    volume_pyramid = pointyShapeVolume(edge, height, True)
    print(f"Volume of the square pyramid: {volume_pyramid:.2f}")

    # Right circular cone
    radius = float(input("\nEnter the radius of the circular base: "))
    height_cone = float(input("Enter the height of the cone: "))
    volume_cone = pointyShapeVolume(radius, height_cone, False)
    print(f"Volume of the right circular cone: {volume_cone:.2f}")

if __name__ == "__main__":
    main()
