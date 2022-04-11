import cdsapi
import urllib3
urllib3.disable_warnings()
c = cdsapi.Client()

c.retrieve(
            'reanalysis-oras5',
                {
                            'format': 'tgz',
                                    'product_type': 'operational',
                                            'vertical_resolution': 'all_levels',
                                                    'variable': [
                                                                    'meridional_velocity', 'zonal_velocity',
                                                                            ],
                                                            'year': [
                                                                            '2015', '2016', '2017',
                                                                                        '2018', '2019', '2020',
                                                                                                    '2021',
                                                                                                            ],
                                                                    'month': [
                                                                                    '01', '02', '03',
                                                                                                '04', '05', '06',
                                                                                                            '07', '08', '09',
                                                                                                                        '10', '11', '12',
                                                                                                                                ],
                                                                        },
                    'download.tar.gz')
