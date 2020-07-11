import itk
from ExampleGenerator import return_example_volume


def main():
    print("Start main()")
    example = return_example_volume()
    example_itk_pointer = itk.GetImageFromArray(example)

    image_type_input = type(example_itk_pointer)

    # Convert input image to itk.SS
    image_type = itk.Image[itk.SS, 3]
    ImageCast = itk.CastImageFilter[image_type_input, image_type].New()
    ImageCast.SetInput(example_itk_pointer)

    # Extract threshold volume from image
    ThresholdFilter = itk.BinaryThresholdImageFilter[image_type, image_type].New()
    ThresholdFilter.SetInput(ImageCast.GetOutput())
    ThresholdFilter.SetLowerThreshold(19)
    ThresholdFilter.SetUpperThreshold(21)
    ThresholdFilter.SetOutsideValue(False)
    ThresholdFilter.SetInsideValue(True)

    # Convert to mesh
    mesh_type = itk.Mesh[itk.D, 3]
    MeshFilter = itk.BinaryMask3DMeshSource[image_type, mesh_type].New()
    MeshFilter.SetInput(ThresholdFilter.GetOutput())
    MeshFilter.SetObjectValue(1)

    # Write file to hdd
    Writer = itk.MeshFileWriter[mesh_type].New()
    Writer.SetFileName("Test.obj")
    Writer.SetInput(MeshFilter.GetOutput())
    Writer.Update()


if __name__ == "__main__":
    main()
