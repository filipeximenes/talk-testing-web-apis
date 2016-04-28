
from tapioca_awesomebikes import Awesomebikes


def tests():
    cli = Awesomebikes(user='f', password='1')

    response = cli.bikes().get()

    assert response().status_code == 200

    response = cli.bikes().post(data={'size': 43, 'color': 'grey'})

    assert response().status_code == 201

    try:
        response = cli.bikes().post(data={'color': 'grey'})
    except Exception as e:
        res = e.client
        assert res().status_code == 400
        assert 'size' in res().data
    else:
        raise Exception("Failed!")

    print("All tests passed!")


if __name__ == '__main__':
    tests()
