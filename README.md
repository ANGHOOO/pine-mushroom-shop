<p align="center">
  <div align="center"><img src="https://github.com/user-attachments/assets/79172db1-c7aa-4f42-b911-35153c3df591" width="40%"/></div>
  <br>
</p>


<p align="center">"자연산 송이의 모든것!"<br> <span>강원송이총판 쇼핑몰</span>을 클론코딩한 API 서버 토이 프로젝트입니다.</p>

<br>
<br>

### 🍄 단순히 쇼핑몰 기능만 구현하지 않았습니다!
* 실제 서비스로 이어지기까지 어떤 과정을 거치는지
* 유지보수성을 위한 객체지향적 설계는 어떻게 이루어져야 하는지
* 냄새나는 코드를 제거해서 읽기 좋은 코드를 만들기 위해서는 어떻게 해야 하는지

대용량 트래픽에도 장애 없이 동작할 수 있도록 성능과 유지보수성을 고려한 서비스를 만들기 위해서, 읽기 좋은 코드, 객체지향적 설계를 위해 노력하였습니다.

<br>
<br>


### 🍄 프로젝트 전체 구성도
<div align="center"><img src="https://github.com/user-attachments/assets/8a71f3ca-578a-45ea-b4de-a443edb21cbd"></div>
<br>
<br>

### 🍄 테이블 ERD
- [테이블 정의서](https://docs.google.com/spreadsheets/d/15J84XUVwE1L5zgDj9VnxLLhqDx1wBpXzy57Fg623Rrg/edit?usp=sharing)
```mermaid
erDiagram
	direction TB
	member {
		BIGINT member_id PK ""
		VARCHAR login_id UK ""
		VARCHAR password  ""
		VARCHAR password_check_question  ""
		VARCHAR password_check_answer  ""
		VARCHAR member_name  ""
		VARCHAR address  ""
		VARCHAR phone_number  ""
		VARCHAR email  ""
		BOOLEAN is_agreed_email  ""
		VARCHAR gender  ""
		DATE birth_date  ""
		TIMESTAMP created_at  ""
		TIMESTAMP updated_at  ""
	}
	product {
		BIGINT product_id PK ""
		VARCHAR product_name UK ""
		VARCHAR seller UK ""
		VARCHAR origin UK ""
		DECIMAL product_price  ""
		INT stock_quantity  ""
		VARCHAR product_status  ""
		BOOLEAN is_deleted  ""
		TIMESTAMP deleted_at  ""
		TIMESTAMP created_at  ""
		TIMESTAMP updated_at  ""
	}
	orders {
		BIGINT order_id PK ""
		BIGINT member_id FK ""
		BIGINT order_status_id FK ""
		TIMESTAMP created_at  ""
		TIMESTAMP updated_at  ""
		TIMESTAMP ordered_at  ""
		VARCHAR category  ""
		BOOLEAN is_deleted  ""
		TIMESTAMP deleted_at  ""
	}
	order_product {
		BIGINT order_product_id PK ""
		BIGINT order_id FK ""
		BIGINT product_id FK ""
		DECIMAL order_product_price  ""
		INT order_product_quantity  ""
		TIMESTAMP created_at  ""
	}
	payment {
		BIGINT payment_id PK ""
		BIGINT order_id FK ""
		BIGINT member_id FK ""
		BIGINT member_coupon_id FK ""
		BIGINT payment_status_id FK ""
		VARCHAR payment_type  ""
		DECIMAL used_points  ""
		DECIMAL points_balance  ""
		TIMESTAMP created_at  ""
		TIMESTAMP paid_at  ""
		BOOLEAN is_deleted  ""
		TIMESTAMP deleted_at  ""
	}
	shipping {
		BIGINT shipping_id PK ""
		BIGINT order_id FK ""
		BIGINT shipping_status_id FK ""
		VARCHAR shipping_status  ""
		VARCHAR shipping_address  ""
		VARCHAR tracking_number  ""
		TIMESTAMP updated_at  ""
		TIMESTAMP shipped_at  ""
		BOOLEAN is_deleted  ""
		TIMESTAMP deleted_at  ""
	}
	coupon {
		BIGINT coupon_id PK ""
		VARCHAR coupon_name  ""
		DECIMAL discount_rate  ""
		VARCHAR description  ""
		TIMESTAMP created_at  ""
		TIMESTAMP updated_at  ""
		TIMESTAMP expired_at  ""
		BOOLEAN is_deleted  ""
		TIMESTAMP deleted_at  ""
	}
	member_coupon {
		BIGINT member_coupon_id PK ""
		BIGINT member_id FK ""
		BIGINT coupon_id FK ""
		BIGINT member_coupon_status_id FK ""
		DECIMAL applied_discount_rate  ""
		TIMESTAMP created_at  ""
		TIMESTAMP updated_at  ""
		TIMESTAMP expired_at  ""
		BOOLEAN is_deleted  ""
		TIMESTAMP deleted_at  ""
	}
	member_coupon_history {
		BIGINT member_coupon_history_id PK ""
		BIGINT member_coupon_id FK ""
		VARCHAR previous_coupon_status  ""
		VARCHAR current_coupon_status  ""
		VARCHAR changed_reason  ""
		TIMESTAMP created_at  ""
	}
	member_coupon_status {
		BIGINT member_coupon_status_id PK ""
		VARCHAR member_coupon_status_category  ""
		TIMESTAMP created_at  ""
		TIMESTAMP updated_at  ""
	}
	payment_cancel {
		BIGINT payment_cancel_id PK ""
		BIGINT payment_id FK ""
		BIGINT member_id FK ""
		TIMESTAMP requested_at  ""
		TIMESTAMP processed_at  ""
		BOOLEAN is_canceled  ""
		VARCHAR cancel_reason  ""
	}
	points_history {
		BIGINT points_history_id PK ""
		BIGINT member_id FK ""
		DECIMAL previous_points_balance  ""
		DECIMAL changed_amount  ""
		DECIMAL current_points_balance  ""
		VARCHAR changed_reason  ""
		TIMESTAMP created_at  ""
	}
	order_status {
		BIGINT order_status_id PK ""
		VARCHAR order_status_category  ""
		TIMESTAMP created_at  ""
		TIMESTAMP updated_at  ""
	}
	payment_status {
		BIGINT payment_status_id PK ""
		VARCHAR payment_status_category  ""
		TIMESTAMP created_at  ""
		TIMESTAMP updated_at  ""
	}
	shipping_status {
		BIGINT shipping_status_id PK ""
		VARCHAR shipping_status_category  ""
		TIMESTAMP created_at  ""
		TIMESTAMP updated_at  ""
	}

	member||--o{orders:"1:N"
	member||--o{payment:"1:N"
	member||--o{payment_cancel:"1:N"
	member||--o{points_history:"1:N"
	member||--o{member_coupon:"1:N"
	orders||--||payment:"1:1"
	orders||--||shipping:"1:1"
	orders||--o{order_product:"1:N"
	orders}o--||order_status:"N:1"
	order_product}o--||product:"N:1"
	payment||--||payment_status:"1:1"
	payment||--||member_coupon:"1:1"
	payment}o--||payment_cancel:"1:N"
	shipping||--||shipping_status:"1:1"
	coupon||--o{member_coupon:"N:1"
	member_coupon||--||member_coupon_status:"1:1"
	member_coupon||--o{member_coupon_history:"N:1"
```
