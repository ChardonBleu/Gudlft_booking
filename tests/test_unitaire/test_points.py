from tests.fixtures import club_one


def test_welcome_for_display_points(logged_client, club_one, mocker):
    mocker.patch('server.research_club_in_clubs_by_email',
                 return_value=club_one)
    response = logged_client.get('/welcome')
    assert response.status_code == 200
    assert b'All clubs points:' in response.data
    expected_b = b'<td>club_test1_name</td>\n                    <td>15</td>'
    assert expected_b in response.data


def test_redirect_if_non_logged(client):
    response = client.get('/welcome')
    assert response.status_code == 302
