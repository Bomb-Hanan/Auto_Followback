# ライブラリの読み込み
import tweepy

#以下4行にて，''内に実行させたいTwitterアカウントの各キーを入力
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

#twitter認証
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# フォロワーを新しい順で取得。
flist= api.get_followers(count=10)

for f in flist:
    f_id = f.id
    # 相手のアカウントの説明文にフォローバックしたくない[キーワード]があればここで登録。
    #（例：副業など）
    if "<>" in f.description:
         continue
    else:
        api.create_friendship(user_id=f_id)
        print(f_id)

# フォロワーの取得
#""内に実行させたいアカウントのIDを入力(＠は除く)
followers = api.get_follower_ids(user_id="")
# フォローユーザーの取得
#""内に実行させたいアカウントのIDを入力(＠は除く)
friends = api.get_friend_ids(user_id="")

# フォローユーザー分だけループ
for f in friends:

    # フォローユーザーがフォロワー一覧に含まれていないなら
    if f not in followers:
        api.destroy_friendship(user_id=f)
        print(f)
