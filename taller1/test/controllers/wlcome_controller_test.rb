require 'test_helper'

class WlcomeControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get wlcome_index_url
    assert_response :success
  end

end
