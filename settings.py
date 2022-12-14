menu = [
    {'name': 'Наши услуги'},
    {'name': 'Отзывы'},
    {'name': 'О нас'},
]
contacts = [
    'тел: +7-777-777-77-77',
    'тел: +7-777-777-77-77',
    'Наш адрес: г.Караганда, ул.Муканова, офис 120',
]
whatsapp = 'https://wa.me/77003475747'
clean_list = [
    {
        'group':'clean_type', 
        'title':'Генеральная уборка', 
        'name':'spring_cleaning',
        'is_range': True,
        'range_min':0,
        'range_max':500,
        'range':[(0, '__0'), (50, '_50'), (100, '100'), (150, '150'), (200, '200'), (250, '250'), (300, '300'), (350, '350'), (400, '400'), (450, '450'), (500, '500')],
        'cost': 250,
    },
    {
        'group':'clean_type', 
        'title':'Влажная уборка', 
        'name':'wet_cleaning',
        'is_range': True,
        'range_min':0,
        'range_max':500,
        'range':[(0, '__0'), (50, '_50'), (100, '100'), (150, '150'), (200, '200'), (250, '250'), (300, '300'), (350, '350'), (400, '400'), (450, '450'), (500, '500')],
        'cost': 350,
    },
    {
        'group':'clean_type', 
        'title':'Уборка после ремонта', 
        'name':'afterepair_cleaning',
        'is_range': True,
        'range_min':0,
        'range_max':500,
        'range':[(0, '__0'), (50, '_50'), (100, '100'), (150, '150'), (200, '200'), (250, '250'), (300, '300'), (350, '350'), (400, '400'), (450, '450'), (500, '500')],
        'cost': 400,
    },
    {
        'group':'room_type', 
        'title':'Жилое помещение', 
        'name':'living_room',
        'is_range': False,
    },
    {
        'group':'room_type', 
        'title':'Частный дом', 
        'name':'private_house', 
        'is_range': False,
    },
    {
        'group':'room_type', 
        'title':'Производственное помещение', 
        'name':'production_room',
        'is_range': False,
    },
    {
        'group':'room_type', 
        'title':'Территория участка', 
        'name':'site_area', 
        'is_range': False,
    },
    {
        'group':'cleanning', 
        'title':'Хим.чистка ковровых покрытий (кв.м)',
        'name':'carpet_cleanning',
        'is_range': True,
        'range_min':0,
        'range_max':50,
        'range':[(0, '_0'), (5, '_5'), (10, '10'), (15, '15'), (20, '20'), (25, '25'), (30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50')],
        'cost':600,
    },
    {
        'group':'cleanning', 
        'title':'Хим.чистка мебели (посадочное место)', 
        'name':'furniture_cleanning', 
        'is_range': True,
        'range_min':0,
        'range_max':30,
        'range': [(0, '_0'), (5, '_5'), (10, '10'), (15, '15'), (20, '20'), (25, '25'), (30, '30')],
        'cost':3000,
    }, 
    {
        'group':'cleanning', 
        'title':'Хим.чистка матрасов', 
        'name':'mattress_cleanning',
        'is_range': True, 
        'range_min':0,
        'range_max':3,
        'range':[(0, '0'), (1, '1'), (2, '1.5'), (3, '2')],
        'cost':6000,
    }, 
    {
        'group':'cleanning', 
        'title':'Мытье окон', 
        'name':'wash_window',
        'is_range': False,
        'cost':3000,
    }, 
    {
        'group':'cleanning', 
        'title': 'Мытье посуды', 
        'name':'wash_up',
        'is_range': False,
        'cost':3500,
    }, 
    {
        'group':'cleanning',
        'title':'Удаление запахов', 
        'name':'odor_removal',
        'is_range': False,
        'cost':3000,
    }, 
    {
        'group':'cleanning', 
        'title': 'Глажка', 
        'name':'ironing',
        'is_range': False,
        'cost':3500,
    }, 
]
