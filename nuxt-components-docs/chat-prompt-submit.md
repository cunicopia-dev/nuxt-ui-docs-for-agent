<!-- source: https://ui.nuxt.com/components/chat-prompt-submit --> # ChatPromptSubmitPRO

[Button](/components/button)[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/ChatPromptSubmit.vue)

A Button for submitting chat prompts with automatic status handling.

## Usage

The ChatPromptSubmit component is used inside the
[ChatPrompt](/components/chat-prompt) component to submit the prompt. It
automatically handles the different `status` values to control the chat.

It extends the [Button](/components/button) component, so you can pass any
property such as `color`, `variant`, `size`, etc.

    
    
    <template>
      <UChatPrompt>
        <UChatPromptSubmit />
      </UChatPrompt>
    </template>
    

You can also use it inside the `footer` slot of the
[`ChatPrompt`](/components/chat-prompt) component.

### Ready

When its status is `ready`, use the `color`, `variant` and `icon` props to
customize the Button. Defaults to:

  * `color="primary"`
  * `variant="solid"`
  * `icon="i-lucide-arrow-up"`

color

primary

variant

solid

icon

    
    
    <template>
      <UChatPromptSubmit color="primary" variant="solid" icon="i-lucide-arrow-up" />
    </template>
    

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.arrowUp` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.arrowUp` key.

### Submitted

When its status is `submitted`, use the `submitted-color`, `submitted-variant`
and `submitted-icon` props to customize the Button. Defaults to:

  * `submittedColor="neutral"`
  * `submittedVariant="subtle"`
  * `submittedIcon="i-lucide-square"`

The `stop` event is emitted when the user clicks on the Button.

submittedColor

neutral

submittedVariant

subtle

submittedIcon

    
    
    <template>
      <UChatPromptSubmit
        submitted-color="neutral"
        submitted-variant="subtle"
        submitted-icon="i-lucide-square"
        status="submitted"
      />
    </template>
    

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.stop` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.stop` key.

### Streaming

When its status is `streaming`, use the `streaming-color`, `streaming-variant`
and `streaming-icon` props to customize the Button. Defaults to:

  * `streamingColor="neutral"`
  * `streamingVariant="subtle"`
  * `streamingIcon="i-lucide-square"`

The `stop` event is emitted when the user clicks on the Button.

streamingColor

neutral

streamingVariant

subtle

streamingIcon

    
    
    <template>
      <UChatPromptSubmit
        streaming-color="neutral"
        streaming-variant="subtle"
        streaming-icon="i-lucide-square"
        status="streaming"
      />
    </template>
    

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.stop` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.stop` key.

### Error

When its status is `error`, use the `error-color`, `error-variant` and `error-
icon` props to customize the Button. Defaults to:

  * `errorColor="error"`
  * `errorVariant="soft"`
  * `errorIcon="i-lucide-rotate-ccw"`

The `reload` event is emitted when the user clicks on the Button.

errorColor

error

errorVariant

soft

errorIcon

    
    
    <template>
      <UChatPromptSubmit
        error-color="error"
        error-variant="soft"
        error-icon="i-lucide-rotate-ccw"
        status="error"
      />
    </template>
    

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.reload` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.reload` key.

## Examples

[](https://sdk.vercel.ai/docs/getting-started/nuxt)These chat components are
designed to be used with the `useChat` composable from **Vercel AI SDK**.

[](https://github.com/nuxt-ui-pro/chat)Check out the source code of our **AI
Chat template** on GitHub for a real-life example.

### Within a page

Use the ChatPromptSubmit component with the `useChat` composable to display a
chat prompt within a page.

Pass the `status` prop and listen to the `stop` and `reload` events to control
the chat.

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
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`status`| `'ready'`| ` "error" | "submitted" | "streaming" | "ready"`  
`streamingColor`| `'neutral'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`streamingVariant`| `'subtle'`| ` "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`  
`submittedColor`| `'neutral'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`submittedVariant`| `'subtle'`| ` "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`  
`errorColor`| `'error'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`errorVariant`| `'soft'`| ` "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`  
`icon`| `appConfig.ui.icons.arrowUp`| ` string`The icon displayed in the
button when the status is `ready`.  
`label`| | ` string`  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`The color of the button when the status is `ready`.  
`size`| `'md'`| ` "md" | "xs" | "sm" | "lg" | "xl"`  
`variant`| `'solid'`| ` "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`The variant of the button when the status is `ready`.  
`streamingIcon`| `appConfig.ui.icons.stop`| ` string`The icon displayed in the
button when the status is `streaming`.  
`submittedIcon`| `appConfig.ui.icons.stop`| ` string`The icon displayed in the
button when the status is `submitted`.  
`errorIcon`| `appConfig.ui.icons.reload`| ` string`The icon displayed in the
button when the status is `error`.  
`ui`| | ` { base?: ClassNameValue; } & { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`Show properties

  * `base?: ClassNameValue`
  * `label?: ClassNameValue`
  * `leadingIcon?: ClassNameValue`
  * `leadingAvatar?: ClassNameValue`
  * `leadingAvatarSize?: ClassNameValue`
  * `trailingIcon?: ClassNameValue`

  
  
### Slots

Slot |  Type   
---|---  
`leading`| `{}`  
`default`| `{}`  
`trailing`| `{}`  
  
### Emits

Event |  Type   
---|---  
`stop`| `[]`  
`reload`| `[]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        chatPromptSubmit: {
          slots: {
            base: ''
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
            chatPromptSubmit: {
              slots: {
                base: ''
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
            chatPromptSubmit: {
              slots: {
                base: ''
              }
            }
          }
        })
      ]
    })
    

Expand code

[ChatPromptAn enhanced Textarea for submitting prompts in AI chat
interfaces.](/components/chat-prompt)[CheckboxAn input element to toggle
between checked and unchecked states.](/components/checkbox)

