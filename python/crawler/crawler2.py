"""
class NaverWebtoonCrawler생성
    초기화메서드
        webtoon_id
        episode_list (빈 list)
            를 할당
    인스턴스 메서드
        def get_episode_list(self, page)
            해당 페이지의 episode_list를 생성, self.episode_list에 할당
        def clear_episode_list(self)
            자신의 episode_list를 빈 리스트로 만듬
        def get_all_episode_list(self)
            webtoon_id의 모든 episode를 생성
        def add_new_episode_list(self)
            새로 업데이트된 episode목록만 생성
"""
import utils


class NaverWebtoonCrawler:
    def __init__(self, webtoon_id):
        self.webtoon_id = webtoon_id
        self.episode_list = list()


    @property
    def total_episode_count(self):
        """
        webtoon_id에 해당하는 실제 웹툰의 총 episode수를 리턴
        requests를 사용
        :return: 총 episode수 (int)
        """
        el = utils.get_webtoon_episode_list(self.webtoon_id)
        return int(el[0].no)


    @property
    def up_to_date(self):
        """
        현재 가지고있는 episode_list가 웹상의 최신 episode까지 가지고 있는지
        :return: boolean값
        """
        el = utils.get_webtoon_episode_list(self.webtoon_id)
        return int(el[0] in self.episode_list )


    def update_episode_list(self, force_update=False):
        """
        self.episode_list에 존재하지 않는 episode들을 self.episode_list에 추가
        :param force_update: 이미 존재하는 episode도 강제로 업데이트
        :return: 추가된 episode의 수 (int)
        """
        el = utils.get_webtoon_episode_list(self.webtoon_id)
        if force_update:
            self.episode_list = el
        else:
            for episode in el:
                if episode in self.episode_list:
                    break
                self.episode_list.append(episode)



    def save(self, path=None):
        """
        현재폴더를 기준으로 db/<webtoon_id>.txt 파일에
        pickle로 self.episode_list를 저장
        :return: 성공여부
        """
        return pickle.dump(self.episode_list, open(f'./db/{self.webtoon_id}.txt', 'wb'))


    def load(self, path=None):
        """
        현재폴더를 기준으로 db/<webtoon_id>.txt 파일의 내용을 불러와
        pickle로 self.episode_list를 복원
        :return:
        """
        pickle.load(open(f'./db/{self.webtoon_id}.txt, 'rb'))


nwc = NaverWebtoonCrawler(651673)
print(nwc.total_episode_count)
