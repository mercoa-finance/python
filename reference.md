# Reference
## EntityGroup
<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all entity groups. If using a JWT, will return all groups the entity is part of. If using an API key, will return all groups for the organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.get_all()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return. Defaults to 1. Max is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[EntityGroupId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an entity group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_group_types import EntityGroupRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.create(
    request=EntityGroupRequest(
        foreign_id="your-group-id",
        name="AcmeConglomerate",
        email_to_name="acmegroup",
        entity_ids=[
            "ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            "ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `EntityGroupRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an entity group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.get(
    entity_group_id="entg_a3582b70-fd04-4888-9185-a640ae9048be",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**return_entity_metadata:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return simple key/value metadata for the specified keys for the entities in the group. For more complex metadata, use the Metadata API.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an entity group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_group_types import EntityGroupRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.update(
    entity_group_id="entg_a3582b70-fd04-4888-9185-a640ae9048be",
    request=EntityGroupRequest(
        foreign_id="your-group-id",
        name="AcmeConglomerate",
        email_to_name="acmegroup",
        entity_ids=[
            "ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            "ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityGroupRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an entity group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.delete(
    entity_group_id="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">get_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a JWT token for an entity group with the given options. This token can be used to authenticate to any entity in the entity group in the Mercoa API and iFrame.

<Warning>We recommend using [this endpoint](/api-reference/entity-group/user/get-token). This will enable features such as approvals and comments.</Warning>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import TokenGenerationOptions

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.get_token(
    entity_group_id="entg_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=TokenGenerationOptions(
        expires_in="1h",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `TokenGenerationOptions` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">add_entities</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add entities to an entity group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_group_types import EntityGroupEntityUpdateRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.add_entities(
    entity_group_id="entg_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=EntityGroupEntityUpdateRequest(
        entity_ids=[
            "ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            "ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityGroupEntityUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">remove_entities</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove entities from an entity group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_group_types import EntityGroupEntityUpdateRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.remove_entities(
    entity_group_id="entg_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=EntityGroupEntityUpdateRequest(
        entity_ids=[
            "ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            "ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityGroupEntityUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EntityGroup User
<details><summary><code>client.entity_group.user.<a href="src/mercoa/entity_group/user/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search entity group users
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.user.find(
    entity_group_id="entg_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    name="John",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — ID used to identify user in your system
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter users by role. If multiple roles are provided, users with any of the roles will be returned.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter users by name. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Filter users by email. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of entities to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[EntityUserId]` — The ID of the user to start after. If not provided, the first page of entities will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.user.<a href="src/mercoa/entity_group/user/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create entity user that will be added to all entities in the group.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_group_types import (
    EntityGroupUserEntityRequest,
    EntityGroupUserRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.user.create(
    entity_group_id="entg_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=EntityGroupUserRequest(
        foreign_id="MY-DB-ID-12345",
        email="john.doe@acme.com",
        name="John Doe",
        entities=[
            EntityGroupUserEntityRequest(
                roles=["admin", "approver"],
                entity_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
            ),
            EntityGroupUserEntityRequest(
                roles=["viewer"],
                entity_id="ent_574s93r-3943-fu39-g9dfr-33b42a55812c",
            ),
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityGroupUserRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.user.<a href="src/mercoa/entity_group/user/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get entity user from a group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.user.get(
    entity_group_id="entg_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    foreign_id="MY-DB-ID-12345",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `str` — ID used to identify user in your system
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.user.<a href="src/mercoa/entity_group/user/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update entity user for all entities in the group.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_group_types import (
    EntityGroupUserEntityRequest,
    EntityGroupUserRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.user.update(
    entity_group_id="entg_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    foreign_id="MY-DB-ID-12345",
    request=EntityGroupUserRequest(
        foreign_id="MY-DB-ID-12345",
        email="john.doe@acme.com",
        name="John Doe",
        entities=[
            EntityGroupUserEntityRequest(
                roles=["admin", "approver"],
                entity_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
            ),
            EntityGroupUserEntityRequest(
                roles=["viewer"],
                entity_id="ent_574s93r-3943-fu39-g9dfr-33b42a55812c",
            ),
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `str` — ID used to identify user in your system
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityGroupUserRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.user.<a href="src/mercoa/entity_group/user/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete entity user from all entities in the group. This will also remove the user from all approval policies. If an approval policy will break as a result of this operation, this request will fail.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.user.delete(
    entity_group_id="string",
    foreign_id="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `str` — ID used to identify user in your system
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.user.<a href="src/mercoa/entity_group/user/client.py">get_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a JWT token for an entity group with the given options. This token can be used to authenticate to any entity in the entity group as the user in the Mercoa API and iFrame.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import TokenGenerationOptions

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.user.get_token(
    entity_group_id="entg_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    foreign_id="MY-DB-ID-12345",
    request=TokenGenerationOptions(
        expires_in="1h",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `str` — ID used to identify user in your system
    
</dd>
</dl>

<dl>
<dd>

**request:** `TokenGenerationOptions` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity
<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search all entities with the given filters. If no filters are provided, all entities will be returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.find(
    is_customer=True,
    foreign_id="MY-DB-ID-12345",
    payment_methods=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_methods:** `typing.Optional[bool]` — If true, will include entity payment methods as part of the response
    
</dd>
</dl>

<dl>
<dd>

**is_customer:** `typing.Optional[bool]` — If true, only entities with a direct relationship to the requesting organization will be returned. If false or not provided, all entities will be returned.
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — ID used to identify this entity in your system
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[EntityStatus, typing.Sequence[EntityStatus]]]` 
    
</dd>
</dl>

<dl>
<dd>

**is_payee:** `typing.Optional[bool]` 

If true, entities that are marked as payees will be returned.
If false or not provided, entities that are marked as payees will not be returned.
    
</dd>
</dl>

<dl>
<dd>

**is_payor:** `typing.Optional[bool]` 

If true or not provided, entities that are marked as payors will be returned.
If false, entities that are marked as payors will not be returned.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter entities by name. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[MetadataFilter]` — Filter entities by simple key/value metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**return_metadata:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return simple key/value metadata for the specified keys for the entities. For more complex metadata, use the Metadata API.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of entities to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[EntityId]` — The ID of the entity to start after. If not provided, the first page of entities will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import (
    BusinessProfileRequest,
    EntityRequest,
    ProfileRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.create(
    request=EntityRequest(
        is_customer=False,
        is_payor=False,
        is_payee=True,
        account_type="business",
        foreign_id="MY-DB-ID-90909",
        profile=ProfileRequest(
            business=BusinessProfileRequest(
                email="vendor@bigboxstore.com",
                legal_business_name="Big Box Store",
                website="http://www.bigboxstore.com",
                business_type="publicCorporation",
            ),
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `EntityRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.get(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**return_metadata:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return simple key/value metadata for the specified keys for the entities. For more complex metadata, use the Metadata API.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.commons import Address, PhoneNumber
from mercoa.entity_types import (
    BusinessProfileRequest,
    Ein,
    EntityUpdateRequest,
    ProfileRequest,
    TaxId,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.update(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=EntityUpdateRequest(
        is_customer=True,
        is_payor=True,
        is_payee=False,
        account_type="business",
        foreign_id="MY-DB-ID-12345",
        profile=ProfileRequest(
            business=BusinessProfileRequest(
                email="customer@acme.com",
                legal_business_name="Acme Inc.",
                website="http://www.acme.com",
                business_type="llc",
                phone=PhoneNumber(
                    country_code="1",
                    number="4155551234",
                ),
                address=Address(
                    address_line_1="123 Main St",
                    address_line_2="Unit 1",
                    city="San Francisco",
                    state_or_province="CA",
                    postal_code="94105",
                    country="US",
                ),
                tax_id=TaxId(
                    ein=Ein(
                        number="12-3456789",
                    ),
                ),
            ),
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Will archive the entity. This action cannot be undone, and the entity will no longer be available for use. The foreignId on the entity will be cleared as well.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.delete(
    entity_id="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">accept_terms_of_service</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is used to indicate acceptance of Mercoa's terms of service for an entity. Send a request to this endpoint only after the entity has accepted the Mercoa ToS. Entities must accept Mercoa ToS before they can be send or pay invoices using Mercoa's payment rails.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.accept_terms_of_service(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">initiate_kyb</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is used to initiate KYB for an entity.
Send a request to this endpoint only after the entity has accepted the Mercoa ToS,
all representatives have been added, and all required fields have been filled out.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.initiate_kyb(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">get_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a JWT token for an entity with the given options. This token can be used to authenticate the entity in the Mercoa API and iFrame.

<Warning>We recommend using [this endpoint](/api-reference/entity/user/get-token). This will enable features such as approvals and comments.</Warning>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import TokenGenerationOptions

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.get_token(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=TokenGenerationOptions(
        expires_in="1h",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `TokenGenerationOptions` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">plaid_link_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a Plaid link token for an entity. This token can be used to add or update a bank account to the entity using Plaid Link.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.plaid_link_token(
    entity_id="string",
    payment_method_id="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**payment_method_id:** `typing.Optional[PaymentMethodId]` — ID of Bank Account to update
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">get_onboarding_link</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate an onboarding link for the entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.get_onboarding_link(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    type="PAYOR",
    expires_in="1h",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**type:** `EntityOnboardingLinkType` — The type of onboarding link to generate. If not provided, the default is payee. The onboarding options are determined by your organization's onboarding configuration.
    
</dd>
</dl>

<dl>
<dd>

**expires_in:** `typing.Optional[str]` — Expressed in seconds or a string describing a time span. The default is 24h.
    
</dd>
</dl>

<dl>
<dd>

**connected_entity_id:** `typing.Optional[EntityId]` — The ID of the entity to connect to. If onboarding a payee, this should be the payor entity ID. If onboarding a payor, this should be the payee entity ID. If no connected entity ID is provided, the onboarding link will be for a standalone entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">send_onboarding_link</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send an email with a onboarding link to the entity. The email will be sent to the email address associated with the entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.send_onboarding_link(
    entity_id="string",
    type="PAYEE",
    expires_in="string",
    connected_entity_id="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**type:** `EntityOnboardingLinkType` — The type of onboarding link to generate. If not provided, the default is payee. The onboarding options are determined by your organization's onboarding configuration.
    
</dd>
</dl>

<dl>
<dd>

**expires_in:** `typing.Optional[str]` — Expressed in seconds or a string describing a time span. The default is 7 days.
    
</dd>
</dl>

<dl>
<dd>

**connected_entity_id:** `typing.Optional[EntityId]` — The ID of the entity to connect to. If onboarding a payee, this should be the payor entity ID. If onboarding a payor, this should be the payee entity ID. If no connected entity ID is provided, the onboarding link will be for a standalone entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all events for an entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.events(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — Start date filter. If not provided, events from the start of time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — End date filter. If not provided, events to the end of time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity EmailLog
<details><summary><code>client.entity.email_log.<a href="src/mercoa/entity/email_log/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all incoming invoice emails for an entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.email_log.find(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of logs to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[EntityId]` — The ID of the log to start after. If not provided, the first page of logs will be returned.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search for logs by email address or subject
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.email_log.<a href="src/mercoa/entity/email_log/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an email log by ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.email_log.get(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    log_id="log_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**log_id:** `EmailLogId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity User
<details><summary><code>client.entity.user.<a href="src/mercoa/entity/user/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all entity users (DEPRECATED, use Search Entity Users)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.get_all(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.user.<a href="src/mercoa/entity/user/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search entity users
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.find(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    name="John",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — ID used to identify user in your system
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter users by role. If multiple roles are provided, users with any of the roles will be returned.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter users by name. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Filter users by email. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of entities to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[EntityUserId]` — The ID of the user to start after. If not provided, the first page of entities will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.user.<a href="src/mercoa/entity/user/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import EntityUserRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.create(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=EntityUserRequest(
        foreign_id="MY-DB-ID-12345",
        email="john.doe@acme.com",
        name="John Doe",
        roles=["admin", "approver"],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityUserRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.user.<a href="src/mercoa/entity/user/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get entity user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.get(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    user_id="user_ec3aafc8-ea86-408a-a6c1-545497badbbb",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `EntityUserId` — User ID or User ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.user.<a href="src/mercoa/entity/user/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update entity user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import EntityUserRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.update(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    user_id="user_ec3aafc8-ea86-408a-a6c1-545497badbbb",
    request=EntityUserRequest(
        foreign_id="MY-DB-ID-12345",
        email="john.doe@acme.com",
        name="John Doe",
        roles=["admin", "approver"],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `EntityUserId` — User ID or User ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityUserRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.user.<a href="src/mercoa/entity/user/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete entity user. This will also remove the user from all approval policies. If an approval policy will break as a result of this operation, this request will fail.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.delete(
    entity_id="string",
    user_id="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `EntityUserId` — User ID or User ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.user.<a href="src/mercoa/entity/user/client.py">get_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a JWT token for an entity user with the given options. This token can be used to authenticate the entity and entity user in the Mercoa API and iFrame.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import TokenGenerationOptions

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.get_token(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    user_id="user_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=TokenGenerationOptions(
        expires_in="1h",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `EntityUserId` — User ID or User ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `TokenGenerationOptions` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Invoice
<details><summary><code>client.invoice.<a href="src/mercoa/invoice/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search invoices for all entities in the organization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.find(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by the ID or foreign ID of the entity that created the invoice.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — Start date filter. Defaults to CREATED_AT unless specified the dateType is specified
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — End date filter. Defaults to CREATED_AT unless specified the dateType is specified
    
</dd>
</dl>

<dl>
<dd>

**date_type:** `typing.Optional[InvoiceDateFilter]` — Type of date to filter by if startDate and endDate filters are provided. Defaults to CREATED_AT.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[InvoiceOrderByField]` — Field to order invoices by. Defaults to CREATED_AT.
    
</dd>
</dl>

<dl>
<dd>

**order_direction:** `typing.Optional[OrderDirection]` — Direction to order invoices by. Defaults to asc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of invoices to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[InvoiceId]` — The ID of the invoice to start after. If not provided, the first page of invoices will be returned.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Find invoices by vendor name, invoice number, or amount. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter invoices by metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**line_item_metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter invoices by line item metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**line_item_gl_account_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter invoices by line item GL account ID. Each filter will be applied as an OR condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**payer_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by payer ID or payer foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**vendor_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by vendor ID or vendor foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**approver_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoices by assigned approver user ID.
    
</dd>
</dl>

<dl>
<dd>

**approver_action:** `typing.Optional[typing.Union[ApproverAction, typing.Sequence[ApproverAction]]]` — Filter invoices by approver action. Needs to be used with approverId. For example, if you want to find all invoices that have been approved by a specific user, you would use approverId and approverAction=APPROVE.
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]]` — Filter invoices by invoice ID.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]]` — Invoice status to filter on
    
</dd>
</dl>

<dl>
<dd>

**payment_type:** `typing.Optional[typing.Sequence[PaymentType]]` — Filter invoices by recurring status
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.<a href="src/mercoa/invoice/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from mercoa import Mercoa
from mercoa.invoice_types import InvoiceCreationWithEntityRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.create(
    request=InvoiceCreationWithEntityRequest(
        status="SCHEDULED",
        payer_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        creator_entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        vendor_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        currency="USD",
        amount=100.0,
        invoice_date=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        due_date=datetime.datetime.fromisoformat(
            "2021-01-31 00:00:00+00:00",
        ),
        payment_source_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        payment_destination_id="pm_5fde2f4a-facc-48ef-8f0d-6b7d087c7b18",
        deduction_date=datetime.datetime.fromisoformat(
            "2021-01-29 00:00:00+00:00",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `InvoiceCreationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.<a href="src/mercoa/invoice/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.get(
    invoice_id="inv_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.<a href="src/mercoa/invoice/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from mercoa import Mercoa
from mercoa.invoice_types import InvoiceUpdateRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.update(
    invoice_id="inv_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=InvoiceUpdateRequest(
        status="SCHEDULED",
        payment_destination_id="pm_5fde2f4a-facc-48ef-8f0d-6b7d087c7b18",
        deduction_date=datetime.datetime.fromisoformat(
            "2021-01-29 00:00:00+00:00",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `InvoiceUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.<a href="src/mercoa/invoice/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Only invoices in the DRAFT and NEW status can be deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.delete(
    invoice_id="inv_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.<a href="src/mercoa/invoice/client.py">events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all events for an invoice
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.events(
    invoice_id="inv_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — Start date filter. If not provided, events from the start of time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — End date filter. If not provided, events to the end of time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Invoice LineItem
<details><summary><code>client.invoice.line_item.<a href="src/mercoa/invoice/line_item/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update invoice line item
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from mercoa import Mercoa
from mercoa.invoice_types import InvoiceLineItemIndividualUpdateRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.line_item.update(
    invoice_id="in_d8f68285-1c6d-4d5a-a9e3-252c3180fac4",
    line_item_id="inli_8aa84cb8-2ae7-4579-8fa3-87586e7c14a7",
    request=InvoiceLineItemIndividualUpdateRequest(
        name="Product A",
        description="Product A",
        service_start_date=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        service_end_date=datetime.datetime.fromisoformat(
            "2021-01-31 00:00:00+00:00",
        ),
        metadata={"key1": "value1", "key2": "value2"},
        gl_account_id="600394",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID
    
</dd>
</dl>

<dl>
<dd>

**line_item_id:** `InvoiceLineItemId` — Invoice Line Item ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `InvoiceLineItemIndividualUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization
<details><summary><code>client.organization.<a href="src/mercoa/organization/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get current organization information
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.organization.get(
    payment_methods=True,
    email_provider=True,
    external_accounting_system_provider=True,
    color_scheme=True,
    payee_onboarding_options=True,
    payor_onboarding_options=True,
    metadata_schema=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_methods:** `typing.Optional[bool]` — include supported payment methods in response
    
</dd>
</dl>

<dl>
<dd>

**email_provider:** `typing.Optional[bool]` — include email provider info in response
    
</dd>
</dl>

<dl>
<dd>

**external_accounting_system_provider:** `typing.Optional[bool]` — include external accounting system provider info in response
    
</dd>
</dl>

<dl>
<dd>

**color_scheme:** `typing.Optional[bool]` — include color scheme info in response
    
</dd>
</dl>

<dl>
<dd>

**payee_onboarding_options:** `typing.Optional[bool]` — include payee onboarding options in response
    
</dd>
</dl>

<dl>
<dd>

**payor_onboarding_options:** `typing.Optional[bool]` — include payor onboarding options in response
    
</dd>
</dl>

<dl>
<dd>

**metadata_schema:** `typing.Optional[bool]` — include metadata schema in response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.<a href="src/mercoa/organization/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update current organization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.organization_types import (
    BusinessOnboardingOptions,
    ColorSchemeRequest,
    EmailProviderRequest,
    EmailSenderRequest,
    ExternalAccountingSystemProviderRequest_None,
    IndividualOnboardingOptions,
    MetadataSchema,
    OnboardingOption,
    OnboardingOptionsRequest,
    OrganizationRequest,
    PaymentMethodsRequest,
    PaymentRailRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.organization.update(
    request=OrganizationRequest(
        name="string",
        logo="string",
        website_url="string",
        support_email="string",
        payment_methods=PaymentMethodsRequest(
            payer_payments=[
                PaymentRailRequest(
                    type="custom",
                    name={"key": "value"},
                    active=True,
                )
            ],
            backup_disbursements=[
                PaymentRailRequest(
                    type="custom",
                    name={"key": "value"},
                    active=True,
                )
            ],
            vendor_disbursements=[
                PaymentRailRequest(
                    type="custom",
                    name={"key": "value"},
                    active=True,
                )
            ],
        ),
        email_provider=EmailProviderRequest(
            sender=EmailSenderRequest(
                provider="none",
                from_email="string",
                from_name="string",
                api_key="string",
            ),
            inbox_domain="string",
            alternative_inbox_domains=[{"key": "value"}],
        ),
        external_accounting_system_provider=ExternalAccountingSystemProviderRequest_None(),
        color_scheme=ColorSchemeRequest(
            primary_color="string",
            secondary_color="string",
            logo_background_color="string",
            rounded_corners=1,
        ),
        payee_onboarding_options=OnboardingOptionsRequest(
            enable_business=True,
            enable_individual=True,
            payment_method=True,
            business=BusinessOnboardingOptions(
                type=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                doing_business_as=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                ein=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                mcc=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                formation_date=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                website=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                description=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                representatives=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                logo=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                average_transaction_size=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                average_monthly_transaction_volume=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                max_transaction_size=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                terms_of_service=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                email=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                name=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                address=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                phone=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                ten_ninety_nine=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                w_9=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
            ),
            individual=IndividualOnboardingOptions(
                date_of_birth=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                ssn=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                terms_of_service=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                email=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                name=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                address=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                phone=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                ten_ninety_nine=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                w_9=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
            ),
        ),
        payor_onboarding_options=OnboardingOptionsRequest(
            enable_business=True,
            enable_individual=True,
            payment_method=True,
            business=BusinessOnboardingOptions(
                type=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                doing_business_as=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                ein=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                mcc=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                formation_date=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                website=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                description=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                representatives=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                logo=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                average_transaction_size=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                average_monthly_transaction_volume=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                max_transaction_size=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                terms_of_service=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                email=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                name=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                address=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                phone=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                ten_ninety_nine=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                w_9=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
            ),
            individual=IndividualOnboardingOptions(
                date_of_birth=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                ssn=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                terms_of_service=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                email=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                name=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                address=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                phone=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                ten_ninety_nine=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
                w_9=OnboardingOption(
                    show=True,
                    edit=True,
                    required=True,
                ),
            ),
        ),
        metadata_schema=[
            MetadataSchema(
                key="string",
                display_name="string",
                description={"key": "value"},
                line_item={"key": "value"},
                type="STRING",
                allow_multiple={"key": "value"},
                validation_rules={"key": "value"},
                show_conditions={"key": "value"},
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `OrganizationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.<a href="src/mercoa/organization/client.py">email_log</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get log of all emails sent to this organization. Content format subject to change.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.organization.email_log(
    start_date=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    end_date=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    limit=1,
    starting_after="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of logs to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — The ID of the log to start after. If not provided, the first page of logs will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## BankLookup
<details><summary><code>client.bank_lookup.<a href="src/mercoa/bank_lookup/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Find bank account details
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.bank_lookup.find(
    routing_number="026009593",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**routing_number:** `str` — Routing number to validate
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Calculate
<details><summary><code>client.calculate.<a href="src/mercoa/calculate/client.py">fee</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Calculate the estimated fees associated with an payment given the amount, payment source, and disbursement method. Can be used to calculate fees for a payment before creating an invoice.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.calculate import CalculateFeesRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.calculate.fee(
    request=CalculateFeesRequest(
        amount=100.0,
        payment_source_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        payment_destination_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CalculateFeesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.calculate.<a href="src/mercoa/calculate/client.py">payment_timing</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Calculate the estimated payment timing given the deduction date, payment source, and disbursement method. Can be used to calculate timing for a payment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from mercoa import Mercoa
from mercoa.calculate import CalculatePaymentTimingRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.calculate.payment_timing(
    request=CalculatePaymentTimingRequest(
        estimated_deduction_date=datetime.datetime.fromisoformat(
            "2024-01-02 00:00:00+00:00",
        ),
        payment_source_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        payment_destination_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CalculatePaymentTimingRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CustomPaymentMethodSchema
<details><summary><code>client.custom_payment_method_schema.<a href="src/mercoa/custom_payment_method_schema/client.py">get_all</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all custom payment method schemas
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.custom_payment_method_schema.get_all()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_payment_method_schema.<a href="src/mercoa/custom_payment_method_schema/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create custom payment method schema
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.payment_method_types import (
    CustomPaymentMethodSchemaField,
    CustomPaymentMethodSchemaRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.custom_payment_method_schema.create(
    request=CustomPaymentMethodSchemaRequest(
        name="Check",
        is_source=False,
        is_destination=True,
        supported_currencies=["USD"],
        fields=[
            CustomPaymentMethodSchemaField(
                name="payToTheOrderOf",
                display_name="Pay To The Order Of",
                type="text",
                optional=False,
            ),
            CustomPaymentMethodSchemaField(
                name="accountNumber",
                display_name="Account Number",
                type="usBankAccountNumber",
                optional=False,
                use_as_account_number=True,
            ),
            CustomPaymentMethodSchemaField(
                name="routingNumber",
                display_name="Routing Number",
                type="usBankRoutingNumber",
                optional=False,
            ),
            CustomPaymentMethodSchemaField(
                name="address",
                display_name="Address",
                type="address",
                optional=False,
            ),
        ],
        estimated_processing_time=7,
        max_amount=50000.0,
        min_amount=1.0,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CustomPaymentMethodSchemaRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_payment_method_schema.<a href="src/mercoa/custom_payment_method_schema/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update custom payment method schema
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.payment_method_types import (
    CustomPaymentMethodSchemaField,
    CustomPaymentMethodSchemaRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.custom_payment_method_schema.update(
    schema_id="cpms_14f78dcd-4614-426e-a37a-7af262431d41",
    request=CustomPaymentMethodSchemaRequest(
        name="Wire",
        is_source=False,
        is_destination=True,
        supported_currencies=["USD", "EUR"],
        fields=[
            CustomPaymentMethodSchemaField(
                name="bankName",
                display_name="Bank Name",
                type="text",
                optional=False,
            ),
            CustomPaymentMethodSchemaField(
                name="recipientName",
                display_name="Recipient Name",
                type="text",
                optional=False,
            ),
            CustomPaymentMethodSchemaField(
                name="accountNumber",
                display_name="Account Number",
                type="usBankAccountNumber",
                optional=False,
                use_as_account_number=True,
            ),
            CustomPaymentMethodSchemaField(
                name="routingNumber",
                display_name="Routing Number",
                type="usBankRoutingNumber",
                optional=False,
            ),
        ],
        estimated_processing_time=0,
        max_amount=100000.0,
        min_amount=1.0,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_id:** `CustomPaymentMethodSchemaId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CustomPaymentMethodSchemaRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_payment_method_schema.<a href="src/mercoa/custom_payment_method_schema/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get custom payment method schema
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.custom_payment_method_schema.get(
    schema_id="cpms_14f78dcd-4614-426e-a37a-7af262431d41",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_id:** `CustomPaymentMethodSchemaId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_payment_method_schema.<a href="src/mercoa/custom_payment_method_schema/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete custom payment method schema. Schema that have been used in an invoice cannot be deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.custom_payment_method_schema.delete(
    schema_id="cpms_14f78dcd-4614-426e-a37a-7af262431d41",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_id:** `CustomPaymentMethodSchemaId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EntityGroup Invoice
<details><summary><code>client.entity_group.invoice.<a href="src/mercoa/entity_group/invoice/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get invoices for an entity group with the given filters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.invoice.find(
    entity_group_id="entg_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    exclude_receivables=True,
    order_by="CREATED_AT",
    order_direction="ASC",
    limit=10,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**exclude_payables:** `typing.Optional[bool]` — Return only invoices that are receivable by the entity.
    
</dd>
</dl>

<dl>
<dd>

**exclude_receivables:** `typing.Optional[bool]` — Return only invoices that are payable by the entity.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — Start date for invoice created on date filter.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — End date for invoice created date filter.
    
</dd>
</dl>

<dl>
<dd>

**date_type:** `typing.Optional[InvoiceDateFilter]` — Type of date to filter by if startDate and endDate filters are provided. Defaults to CREATED_AT.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[InvoiceOrderByField]` — Field to order invoices by. Defaults to CREATED_AT.
    
</dd>
</dl>

<dl>
<dd>

**order_direction:** `typing.Optional[OrderDirection]` — Direction to order invoices by. Defaults to asc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of invoices to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[InvoiceId]` — The ID of the invoice to start after. If not provided, the first page of invoices will be returned.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter invoices by metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Find invoices by vendor name, invoice number, or amount. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**payer_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by payer ID or payer foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**vendor_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by vendor ID or vendor foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**approver_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoices by assigned approver user ID.
    
</dd>
</dl>

<dl>
<dd>

**approver_action:** `typing.Optional[typing.Union[ApproverAction, typing.Sequence[ApproverAction]]]` — Filter invoices by approver action. Needs to be used with approverId. For example, if you want to find all invoices that have been approved by a specific user, you would use approverId and approverAction=APPROVE.
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]]` — Filter invoices by invoice ID.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]]` — Invoice status to filter on.
    
</dd>
</dl>

<dl>
<dd>

**payment_type:** `typing.Optional[typing.Sequence[PaymentType]]` — Filter invoices by recurring status
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.invoice.<a href="src/mercoa/entity_group/invoice/client.py">metrics</a>(...)</code></summary>
