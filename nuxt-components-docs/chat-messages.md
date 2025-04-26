<!-- source: https://ui.nuxt.com/components/chat-messages --> # ChatMessagesPRO

[AI SDK](https://sdk.vercel.ai/)[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/ChatMessages.vue)

Display a list of chat messages, designed to work seamlessly with Vercel AI
SDK.

## Usage

The ChatMessages component displays a list of [ChatMessage](/components/chat-
message) components using either the default slot or the `messages` prop.

    
    
    <template>
      <UChatMessages>
        <UChatMessage
          v-for="(message, index) in messages"
          :key="index"
          v-bind="message"
        />
      </UChatMessages>
    </template>
    

This component is purpose-built for AI chatbots with features like:

  * Initial scroll to the bottom upon loading (`shouldScrollToBottom`).
  * Continuous scrolling down as new messages arrive (`shouldAutoScroll`).
  * An "Auto scroll" button appears when scrolled up, allowing users to jump back to the latest messages (`autoScroll`).
  * A loading indicator displays while the assistant is processing (`status`).
  * Submitted messages are scrolled to the top of the viewport and the height of the last user message is dynamically adjusted.

### Messages

Use the `messages` prop to display a list of chat messages.

Hello, how are you?

I am doing well, thank you for asking! How can I assist you today?

What is the current weather in Tokyo?

Based on the latest data, Tokyo is currently experiencing sunny weather with
temperatures around 24°C (75°F). It's a beautiful day with clear skies.

    
    
    <script setup lang="ts">
    const messages = ref([
      {
        id: '6045235a-a435-46b8-989d-2df38ca2eb47',
        role: 'user',
        content: 'Hello, how are you?'
      },
      {
        id: '7a92b3c1-d5f8-4e76-b8a9-3c1e5fb2e0d8',
        role: 'assistant',
        content: 'I am doing well, thank you for asking! How can I assist you today?'
      },
      {
        id: '9c84d6a7-8b23-4f12-a1d5-e7f3b9c05e2a',
        role: 'user',
        content: 'What is the current weather in Tokyo?'
      },
      {
        id: 'b2e5f8c3-a1d9-4e67-b3f2-c9d8e7a6b5f4',
        role: 'assistant',
        content:
          "Based on the latest data, Tokyo is currently experiencing sunny weather with temperatures around 24°C (75°F). It's a beautiful day with clear skies."
      }
    ])
    </script>
    
    <template>
      <UChatMessages :messages="messages" />
    </template>
    

### Status

Use the `status` prop to display a visual indicator when the assistant is
processing.

Hello, how are you?

    
    
    <script setup lang="ts">
    const messages = ref([
      {
        id: '6045235a-a435-46b8-989d-2df38ca2eb47',
        role: 'user',
        content: 'Hello, how are you?'
      }
    ])
    </script>
    
    <template>
      <UChatMessages status="submitted" :messages="messages" />
    </template>
    

Here's the detail of the different statuses sent by the `useChat` composable:

  * `submitted`: The message has been sent to the API and we're awaiting the start of the response stream.
  * `streaming`: The response is actively streaming in from the API, receiving chunks of data.
  * `ready`: The full response has been received and processed; a new user message can be submitted.
  * `error`: An error occurred during the API request, preventing successful completion.

### User

Use the `user` prop to change the [ChatMessage](/components/chat-message)
props for `user` messages. Defaults to:

  * `side: 'right'`
  * `variant: 'soft'`

user.side

left

user.variant

solid

![](https://github.com/benjamincanac.png)

Hello, how are you?

I am doing well, thank you for asking! How can I assist you today?

![](https://github.com/benjamincanac.png)

What is the current weather in Tokyo?

Based on the latest data, Tokyo is currently experiencing sunny weather with
temperatures around 24°C (75°F). It's a beautiful day with clear skies.

    
    
    <script setup lang="ts">
    const messages = ref([
      {
        id: '6045235a-a435-46b8-989d-2df38ca2eb47',
        role: 'user',
        content: 'Hello, how are you?'
      },
      {
        id: '7a92b3c1-d5f8-4e76-b8a9-3c1e5fb2e0d8',
        role: 'assistant',
        content: 'I am doing well, thank you for asking! How can I assist you today?'
      },
      {
        id: '9c84d6a7-8b23-4f12-a1d5-e7f3b9c05e2a',
        role: 'user',
        content: 'What is the current weather in Tokyo?'
      },
      {
        id: 'b2e5f8c3-a1d9-4e67-b3f2-c9d8e7a6b5f4',
        role: 'assistant',
        content:
          "Based on the latest data, Tokyo is currently experiencing sunny weather with temperatures around 24°C (75°F). It's a beautiful day with clear skies."
      }
    ])
    </script>
    
    <template>
      <UChatMessages
        :user="{
          side: 'left',
          variant: 'solid',
          avatar: {
            src: 'https://github.com/benjamincanac.png'
          }
        }"
        :messages="messages"
      />
    </template>
    

### Assistant

Use the `assistant` prop to change the [ChatMessage](/components/chat-message)
props for `assistant` messages. Defaults to:

  * `side: 'left'`
  * `variant: 'naked'`

assistant.side

left

assistant.variant

outline

Hello, how are you?

I am doing well, thank you for asking! How can I assist you today?

What is the current weather in Tokyo?

Based on the latest data, Tokyo is currently experiencing sunny weather with
temperatures around 24°C (75°F). It's a beautiful day with clear skies.

    
    
    <script setup lang="ts">
    const messages = ref([
      {
        id: '6045235a-a435-46b8-989d-2df38ca2eb47',
        role: 'user',
        content: 'Hello, how are you?'
      },
      {
        id: '7a92b3c1-d5f8-4e76-b8a9-3c1e5fb2e0d8',
        role: 'assistant',
        content: 'I am doing well, thank you for asking! How can I assist you today?'
      },
      {
        id: '9c84d6a7-8b23-4f12-a1d5-e7f3b9c05e2a',
        role: 'user',
        content: 'What is the current weather in Tokyo?'
      },
      {
        id: 'b2e5f8c3-a1d9-4e67-b3f2-c9d8e7a6b5f4',
        role: 'assistant',
        content:
          "Based on the latest data, Tokyo is currently experiencing sunny weather with temperatures around 24°C (75°F). It's a beautiful day with clear skies."
      }
    ])
    </script>
    
    <template>
      <UChatMessages
        :assistant="{
          side: 'left',
          variant: 'outline',
          avatar: {
            icon: 'i-lucide-bot'
          },
          actions: [
            {
              label: 'Copy to clipboard',
              icon: 'i-lucide-copy'
            }
          ]
        }"
        :messages="messages"
      />
    </template>
    

### Auto Scroll

Use the `auto-scroll` prop to customize or hide the auto scroll button (with
`false` value) displayed when scrolling to the top of the chat. Defaults to:

  * `color: 'neutral'`
  * `variant: 'outline'`

You can pass any property from the [Button](/components/button) component to
customize it.

Hello, how are you?

I am doing well, thank you for asking! How can I assist you today?

What is the current weather in Tokyo?

Based on the latest data, Tokyo is currently experiencing sunny weather with
temperatures around 24°C (75°F). It's a beautiful day with clear skies. The
forecast for the rest of the week shows a slight chance of rain on Thursday,
with temperatures gradually rising to 28°C by the weekend. Humidity levels are
moderate at around 65%, and wind speeds are light at 8 km/h from the
southeast. Air quality is good with an index of 42. The UV index is high at 7,
so it's recommended to wear sunscreen if you're planning to spend time
outdoors. Sunrise was at 5:24 AM and sunset will be at 6:48 PM, giving Tokyo
approximately 13 hours and 24 minutes of daylight today. The moon is currently
in its waxing gibbous phase.

Can you recommend some popular tourist attractions in Kyoto?

Kyoto is known for its beautiful temples, traditional tea houses, and gardens.
Some popular attractions include Kinkaku-ji (Golden Pavilion) with its
stunning gold leaf exterior reflecting in the mirror pond, Fushimi Inari
Shrine with its thousands of vermilion torii gates winding up the
mountainside, Arashiyama Bamboo Grove where towering stalks create an
otherworldly atmosphere, Kiyomizu-dera Temple perched on a hillside offering
panoramic views of the city, and the historic Gion district where you might
spot geisha hurrying to evening appointments through narrow stone-paved
streets lined with traditional wooden machiya houses.

    
    
    <script setup lang="ts">
    const messages = ref([
      {
        id: '6045235a-a435-46b8-989d-2df38ca2eb47',
        role: 'user',
        content: 'Hello, how are you?'
      },
      {
        id: '7a92b3c1-d5f8-4e76-b8a9-3c1e5fb2e0d8',
        role: 'assistant',
        content: 'I am doing well, thank you for asking! How can I assist you today?'
      },
      {
        id: '9c84d6a7-8b23-4f12-a1d5-e7f3b9c05e2a',
        role: 'user',
        content: 'What is the current weather in Tokyo?'
      },
      {
        id: 'b2e5f8c3-a1d9-4e67-b3f2-c9d8e7a6b5f4',
        role: 'assistant',
        content:
          "Based on the latest data, Tokyo is currently experiencing sunny weather with temperatures around 24°C (75°F). It's a beautiful day with clear skies. The forecast for the rest of the week shows a slight chance of rain on Thursday, with temperatures gradually rising to 28°C by the weekend. Humidity levels are moderate at around 65%, and wind speeds are light at 8 km/h from the southeast. Air quality is good with an index of 42. The UV index is high at 7, so it's recommended to wear sunscreen if you're planning to spend time outdoors. Sunrise was at 5:24 AM and sunset will be at 6:48 PM, giving Tokyo approximately 13 hours and 24 minutes of daylight today. The moon is currently in its waxing gibbous phase."
      },
      {
        id: 'c3e5f8c3-a1d9-4e67-b3f2-c9d8e7a6b5f4',
        role: 'user',
        content: 'Can you recommend some popular tourist attractions in Kyoto?'
      },
      {
        id: 'd4f5g8c3-a1d9-4e67-b3f2-c9d8e7a6b5f4',
        role: 'assistant',
        content:
          'Kyoto is known for its beautiful temples, traditional tea houses, and gardens. Some popular attractions include Kinkaku-ji (Golden Pavilion) with its stunning gold leaf exterior reflecting in the mirror pond, Fushimi Inari Shrine with its thousands of vermilion torii gates winding up the mountainside, Arashiyama Bamboo Grove where towering stalks create an otherworldly atmosphere, Kiyomizu-dera Temple perched on a hillside offering panoramic views of the city, and the historic Gion district where you might spot geisha hurrying to evening appointments through narrow stone-paved streets lined with traditional wooden machiya houses.'
      }
    ])
    </script>
    
    <template>
      <UChatMessages
        :auto-scroll="{
          color: 'neutral',
          variant: 'outline'
        }"
        :should-scroll-to-bottom="false"
        :messages="messages"
      />
    </template>
    

Expand code

### Auto Scroll Icon

Use the `auto-scroll-icon` prop to customize the auto scroll button
[Icon](/components/icon). Defaults to `i-lucide-arrow-down`.

autoScrollIcon

Hello, how are you?

I am doing well, thank you for asking! How can I assist you today?

What is the current weather in Tokyo?

Based on the latest data, Tokyo is currently experiencing sunny weather with
temperatures around 24°C (75°F). It's a beautiful day with clear skies. The
forecast for the rest of the week shows a slight chance of rain on Thursday,
with temperatures gradually rising to 28°C by the weekend. Humidity levels are
moderate at around 65%, and wind speeds are light at 8 km/h from the
southeast. Air quality is good with an index of 42. The UV index is high at 7,
so it's recommended to wear sunscreen if you're planning to spend time
outdoors. Sunrise was at 5:24 AM and sunset will be at 6:48 PM, giving Tokyo
approximately 13 hours and 24 minutes of daylight today. The moon is currently
in its waxing gibbous phase.

Can you recommend some popular tourist attractions in Kyoto?

Kyoto is known for its beautiful temples, traditional tea houses, and gardens.
Some popular attractions include Kinkaku-ji (Golden Pavilion) with its
stunning gold leaf exterior reflecting in the mirror pond, Fushimi Inari
Shrine with its thousands of vermilion torii gates winding up the
mountainside, Arashiyama Bamboo Grove where towering stalks create an
otherworldly atmosphere, Kiyomizu-dera Temple perched on a hillside offering
panoramic views of the city, and the historic Gion district where you might
spot geisha hurrying to evening appointments through narrow stone-paved
streets lined with traditional wooden machiya houses.

    
    
    <script setup lang="ts">
    const messages = ref([
      {
        id: '6045235a-a435-46b8-989d-2df38ca2eb47',
        role: 'user',
        content: 'Hello, how are you?'
      },
      {
        id: '7a92b3c1-d5f8-4e76-b8a9-3c1e5fb2e0d8',
        role: 'assistant',
        content: 'I am doing well, thank you for asking! How can I assist you today?'
      },
      {
        id: '9c84d6a7-8b23-4f12-a1d5-e7f3b9c05e2a',
        role: 'user',
        content: 'What is the current weather in Tokyo?'
      },
      {
        id: 'b2e5f8c3-a1d9-4e67-b3f2-c9d8e7a6b5f4',
        role: 'assistant',
        content:
          "Based on the latest data, Tokyo is currently experiencing sunny weather with temperatures around 24°C (75°F). It's a beautiful day with clear skies. The forecast for the rest of the week shows a slight chance of rain on Thursday, with temperatures gradually rising to 28°C by the weekend. Humidity levels are moderate at around 65%, and wind speeds are light at 8 km/h from the southeast. Air quality is good with an index of 42. The UV index is high at 7, so it's recommended to wear sunscreen if you're planning to spend time outdoors. Sunrise was at 5:24 AM and sunset will be at 6:48 PM, giving Tokyo approximately 13 hours and 24 minutes of daylight today. The moon is currently in its waxing gibbous phase."
      },
      {
        id: 'c3e5f8c3-a1d9-4e67-b3f2-c9d8e7a6b5f4',
        role: 'user',
        content: 'Can you recommend some popular tourist attractions in Kyoto?'
      },
      {
        id: 'd4f5g8c3-a1d9-4e67-b3f2-c9d8e7a6b5f4',
        role: 'assistant',
        content:
          'Kyoto is known for its beautiful temples, traditional tea houses, and gardens. Some popular attractions include Kinkaku-ji (Golden Pavilion) with its stunning gold leaf exterior reflecting in the mirror pond, Fushimi Inari Shrine with its thousands of vermilion torii gates winding up the mountainside, Arashiyama Bamboo Grove where towering stalks create an otherworldly atmosphere, Kiyomizu-dera Temple perched on a hillside offering panoramic views of the city, and the historic Gion district where you might spot geisha hurrying to evening appointments through narrow stone-paved streets lined with traditional wooden machiya houses.'
      }
    ])
    </script>
    
    <template>
      <UChatMessages
        auto-scroll-icon="i-lucide-chevron-down"
        :should-scroll-to-bottom="false"
        :messages="messages"
      />
    </template>
    

Expand code

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.arrowDown` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.arrowDown` key.

### Should Auto Scroll

Use the `should-auto-scroll` prop to enable/disable continuous auto scroll
while messages are streaming. Defaults to `false`.

    
    
    <template>
      <UChatMessages :messages="messages" should-auto-scroll />
    </template>
    

### Should Scroll To Bottom

Use the `should-scroll-to-bottom` prop to enable/disable bottom auto scroll
when the component is mounted. Defaults to `true`.

    
    
    <template>
      <UChatMessages :messages="messages" :should-scroll-to-bottom="false" />
    </template>
    

## Examples

[](https://sdk.vercel.ai/docs/getting-started/nuxt)These chat components are
designed to be used with the `useChat` composable from **Vercel AI SDK**.

[](https://github.com/nuxt-ui-pro/chat)Check out the source code of our **AI
Chat template** on GitHub for a real-life example.

### Within a page

Use the ChatMessages component with the `useChat` composable to display a list
of chat messages within a page.

Pass the `messages` prop alongside the `status` prop that will be used for the
auto scroll and the indicator display.

pages/[id].vue

    
    
    <script setup lang="ts">
    import { useChat } from '@ai-sdk/vue'
    
    const { messages, input, handleSubmit, reload, stop, status, error } = useChat()
    </script>
    
    <template>
      <UDashboardPanel>
        <template #body>
          <UContainer>
            <UChatMessages :messages="messages" :status="status">
              <template #content="{ message }">
                <MDC :value="message.content" :cache-key="message.id" unwrap="p" />
              </template>
            </UChatMessages>
          </UContainer>
        </template>
    
        <template #footer>
          <UContainer>
            <UChatPrompt v-model="input" :error="error" @submit="handleSubmit">
              <UChatPromptSubmit :status="status" @stop="stop" @reload="reload" />
            </UChatPrompt>
          </UContainer>
        </template>
      </UDashboardPanel>
    </template>
    

In this example, we use the `MDC` component from
[`@nuxtjs/mdc`](https://github.com/nuxt-modules/mdc) to render the content of
the message. As Nuxt UI Pro provides pre-styled prose components, your content
will be automatically styled.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`autoScroll`| `true`| `boolean | Partial<ButtonProps>`  
`shouldAutoScroll`| `false`| `boolean`  
`shouldScrollToBottom`| `true`| `boolean`  
`spacingOffset`| `0`| ` number`  
`messages`| | ` Message[]`Show properties

  * `id: string`A unique identifier for the message.
  * `createdAt?: Date`The timestamp of the message.
  * `content: string`Text content of the message. Use parts when possible.
  * `reasoning?: string`Reasoning for the message.
  * `experimental_attachments?: Attachment[]`Additional attachments to be sent along with the message.
  * `role: "data" | "user" | "system" | "assistant"`The 'data' role is deprecated.
  * `data?: JSONValue`For data messages.
  * `annotations?: JSONValue[]`Additional message-specific information added on the server via StreamData
  * `toolInvocations?: ToolInvocation[]`Tool invocations (that can be tool calls or tool results, depending on whether or not the invocation has finished) that the assistant made as part of this message.
  * `parts?: (TextUIPart | ReasoningUIPart | ToolInvocationUIPart | SourceUIPart | FileUIPart | StepStartUIPart)[]`The parts of the message. Use this for rendering the message in the UI.Assistant messages can have text, reasoning and tool invocation parts. User messages can have text parts.

  
`user`| | ` Pick<ChatMessageProps, "icon" | "variant" | "avatar" | "side" | "actions">`The `user` messages props. `{ side: 'right', variant: 'soft' }`  
`compact`| `false`| `boolean`Render the messages in a compact style. This is
done automatically when used inside a `UChatPalette`.  
`assistant`| | ` Pick<ChatMessageProps, "icon" | "variant" | "avatar" | "side" | "actions">`The `assistant` messages props. `{ side: 'left', variant: 'naked' }`  
`status`| | ` "error" | "submitted" | "streaming" | "ready"`  
`autoScrollIcon`| `appConfig.ui.icons.arrowDown`| ` string`The icon displayed
in the auto scroll button.  
`ui`| | ` { root?: ClassNameValue; indicator?: ClassNameValue; viewport?: ClassNameValue; autoScroll?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
`indicator`| `{}`  
`viewport`| `{ onClick: () => void; }`  
`content`| `{ message: Message; }`  
`leading`| `{ message: Message; }`  
`actions`| `{ message: Message; }`  
  
You can use all the slots of the [`ChatMessage`](/components/chat-
message#slots) component inside ChatMessages, they are automatically forwarded
allowing you to customize individual messages when using the `messages` prop.

    
    
    <template>
      <UChatMessages :messages="messages" :status="status">
        <template #content="{ message }">
          <MDC :value="message.content" :cache-key="message.id" unwrap="p" />
        </template>
      </UChatMessages>
    </template>
    

## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        chatMessages: {
          slots: {
            root: 'w-full flex flex-col gap-1 flex-1 px-2.5 [&>article]:last-of-type:min-h-(--last-message-height)',
            indicator: 'h-6 flex items-center gap-1 py-3 *:size-2 *:rounded-full *:bg-elevated [&>*:nth-child(1)]:animate-[bounce_1s_infinite] [&>*:nth-child(2)]:animate-[bounce_1s_0.15s_infinite] [&>*:nth-child(3)]:animate-[bounce_1s_0.3s_infinite]',
            viewport: 'absolute inset-x-0 top-[86%] data-[state=open]:animate-[fade-in_200ms_ease-out] data-[state=closed]:animate-[fade-out_200ms_ease-in]',
            autoScroll: 'rounded-full absolute right-1/2 translate-x-1/2 bottom-0'
          },
          variants: {
            compact: {
              true: '',
              false: ''
            }
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          uiPro: {
            chatMessages: {
              slots: {
                root: 'w-full flex flex-col gap-1 flex-1 px-2.5 [&>article]:last-of-type:min-h-(--last-message-height)',
                indicator: 'h-6 flex items-center gap-1 py-3 *:size-2 *:rounded-full *:bg-elevated [&>*:nth-child(1)]:animate-[bounce_1s_infinite] [&>*:nth-child(2)]:animate-[bounce_1s_0.15s_infinite] [&>*:nth-child(3)]:animate-[bounce_1s_0.3s_infinite]',
                viewport: 'absolute inset-x-0 top-[86%] data-[state=open]:animate-[fade-in_200ms_ease-out] data-[state=closed]:animate-[fade-out_200ms_ease-in]',
                autoScroll: 'rounded-full absolute right-1/2 translate-x-1/2 bottom-0'
              },
              variants: {
                compact: {
                  true: '',
                  false: ''
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          uiPro: {
            chatMessages: {
              slots: {
                root: 'w-full flex flex-col gap-1 flex-1 px-2.5 [&>article]:last-of-type:min-h-(--last-message-height)',
                indicator: 'h-6 flex items-center gap-1 py-3 *:size-2 *:rounded-full *:bg-elevated [&>*:nth-child(1)]:animate-[bounce_1s_infinite] [&>*:nth-child(2)]:animate-[bounce_1s_0.15s_infinite] [&>*:nth-child(3)]:animate-[bounce_1s_0.3s_infinite]',
                viewport: 'absolute inset-x-0 top-[86%] data-[state=open]:animate-[fade-in_200ms_ease-out] data-[state=closed]:animate-[fade-out_200ms_ease-in]',
                autoScroll: 'rounded-full absolute right-1/2 translate-x-1/2 bottom-0'
              },
              variants: {
                compact: {
                  true: '',
                  false: ''
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

[ChatMessageDisplay a chat message with icon, avatar, and
actions.](/components/chat-message)[ChatPaletteA chat palette to create a
chatbot interface inside an overlay.](/components/chat-palette)

