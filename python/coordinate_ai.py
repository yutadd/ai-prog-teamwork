class CoordinateAI:
    def __init__(self):
        self.coordinate_rules = {
            'Clear': {
                'hot': {
                    'tops': ['半袖Tシャツ', 'ノースリーブ'],
                    'bottoms': ['ショートパンツ', 'スカート'],
                    'accessories': ['帽子', 'サングラス'],
                    'advice': '日差しが強いので、日焼け対策をお忘れなく！'
                },
                'mild': {
                    'tops': ['長袖シャツ', '薄手のセーター'],
                    'bottoms': ['チノパン', 'ジーンズ'],
                    'accessories': ['サングラス'],
                    'advice': '快適な気温ですが、日差しには注意してください。'
                },
                'cold': {
                    'tops': ['セーター', 'コート'],
                    'bottoms': ['暖かいパンツ', 'デニム'],
                    'accessories': ['マフラー', '手袋'],
                    'advice': '晴れていても寒いので、暖かい服装がおすすめです。'
                }
            },
            'Rain': {
                'hot': {
                    'tops': ['半袖シャツ', '薄手のパーカー'],
                    'bottoms': ['長めのパンツ'],
                    'accessories': ['折りたたみ傘', 'レインブーツ'],
                    'advice': '蒸し暑いので、通気性の良い素材を選びましょう。'
                },
                'mild': {
                    'tops': ['レインコート', '長袖シャツ'],
                    'bottoms': ['撥水パンツ'],
                    'accessories': ['傘', 'レインブーツ'],
                    'advice': '雨具をお忘れなく！'
                },
                'cold': {
                    'tops': ['レインコート', '厚手のセーター'],
                    'bottoms': ['暖かいパンツ'],
                    'accessories': ['傘', '防水ブーツ', 'マフラー'],
                    'advice': '雨と寒さ対策の両方が必要です。'
                }
            }
        }

    def get_temperature_category(self, temp):
        if temp >= 25:
            return 'hot'
        elif temp >= 15:
            return 'mild'
        else:
            return 'cold'

    def get_coordinate(self, weather_data):
        weather_main = 'Clear' if weather_data['weather'] in ['Clear', 'Clouds'] else 'Rain'
        temp_category = self.get_temperature_category(weather_data['temperature'])
        
        return self.coordinate_rules[weather_main][temp_category]

