
class ImageryType:

    SkySatScene = 'SkySat Scene'
    SkySatCollect = 'SkySat Collect'
    PSScene = 'PlanetScope Scene'
    PSOrthoTile = 'PlanetScope Ortho Tile'
    REBasicScene = 'RapidEye Basic Scene'
    REOrthoTile = 'RapidEye Ortho Tile'
    Sentinel2Tile = 'Sentinel-2 Tile'
    Landsat8Scene = 'Landsat 8 Scene'


class PSOnlyFilters:

    NearInfrared = 'Near-infrared (NIR)'
    CoastalBGYR = 'Coastal blue, green II, yellow, red edge'
    DoveClassic = 'Dove Classic (PS2)'
    DoveR = 'Dove R (PS2.SD)'
    SuperDove = 'Super Dove (PSB.SD)'


class EnvConditions:

    AreaCoverage = 'Area coverage'
    CloudCover = 'Cloud cover'
    GroundSampleDistance = 'Ground sample distance'
    OffNadirAngle = 'Off-nadir angle'
    SunAzimuth = 'Sun azimuth'
    SunElevation = 'Sun elevation'


class AdvancedFilters:

    FullCatalog = 'Show full catalog'
    SurfaceReflectanceOnly = 'Include only surface reflectance'
    GroundControlOnly = 'Include only results with ground control'
    standardQuality = 'Show only standard image quality'
